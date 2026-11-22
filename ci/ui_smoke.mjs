// Review screen of a finished check, in a real browser: cards, playback, keyboard marks, tabs.
//   node ci/ui_smoke.mjs http://127.0.0.1:8000 <job id> <out dir>
// Exit code 0 = passed.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const [base, jid, out] = process.argv.slice(2);
fs.mkdirSync(out, { recursive: true });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let fails = 0;
function ok(cond, what) {
  console.log((cond ? 'ok    ' : 'FAIL  ') + what);
  if (!cond) fails++;
}

const browser = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));

  await page.goto(base + '/jobs/' + jid);
  await page.waitForSelector('#issues .issue', { timeout: 60000 });
  await page.waitForFunction(() => document.getElementById('audio').readyState >= 1, null, { timeout: 60000 });
  const n = await page.$$eval('#issues .issue', (x) => x.length);
  ok(n >= 2, '검토할 곳 카드: ' + n + '개');
  ok(await page.$eval('#issues .issue', (e) => e.classList.contains('cur')), '첫 카드가 선택됨');
  await page.screenshot({ path: path.join(out, 'review.png') });

  // keyboard: next card plays its part of the recording
  await page.keyboard.press('ArrowDown');
  await sleep(800);
  const st = await page.evaluate(() => {
    const a = document.getElementById('audio');
    const c = document.querySelector('#issues .issue.cur');
    return { idx: [...document.querySelectorAll('#issues .issue')].indexOf(c), paused: a.paused, t: a.currentTime };
  });
  ok(st.idx === 1 && !st.paused && st.t > 0, '↓로 다음 카드 선택과 재생: ' + JSON.stringify(st));
  await page.keyboard.press('Space');

  // marks are saved on the program's side
  const id = await page.$eval('#issues .issue.cur', (e) => e.dataset.id);
  await page.keyboard.press('Digit1');
  await sleep(500);
  const marks = await page.evaluate(async (j) => (await fetch('/api/jobs/' + j + '/marks')).json(), jid);
  ok(marks[id] === 'bad', '1(오독 맞음) 표시가 저장됨: ' + JSON.stringify(marks));

  // the other tabs
  await page.click('#tab-noise');
  await sleep(300);
  ok(await page.$eval('#noise', (e) => !e.hidden), '노이즈 탭 열림');
  await page.click('#tab-lines');
  await page.waitForSelector('#lines .lrow');
  const rows = await page.$$eval('#lines .lrow', (x) => x.length);
  ok(rows === 8, '전체 문장 탭: ' + rows + '문장');
  await page.click('#lines .lrow:nth-child(2) .tc');
  await sleep(800);
  ok(!(await page.evaluate(() => document.getElementById('audio').paused)), '문장 ▶로 그 문장 재생');
  await page.screenshot({ path: path.join(out, 'lines.png') });

  // start page lists the check, and the guide link is there
  await page.goto(base + '/');
  await page.waitForSelector('.ritem');
  ok((await page.$$eval('.ritem', (x) => x.length)) >= 1, '처음 화면 최근 검사 목록');
  ok(!!(await page.$('a[href="/guide"]')), '사용법 단추');
  await page.screenshot({ path: path.join(out, 'home.png') });
  ok(errors.length === 0, '화면 스크립트 오류 없음' + (errors.length ? ': ' + errors.join(' | ') : ''));
} catch (e) {
  ok(false, '화면 시험 중 오류: ' + e.message);
} finally {
  await browser.close();
}
console.log(fails ? `\n실패 ${fails}건` : '\n통과');
process.exit(fails ? 1 : 0);
