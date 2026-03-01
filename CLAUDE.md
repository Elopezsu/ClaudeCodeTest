# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Games

Open any HTML file directly in a browser — no server, build step, or dependencies required.

```bash
open index.html      # Tic Tac Toe
open shooter.html    # Retro top-down shooter
```

## Git Workflow

Every meaningful change must be committed with a clean message and pushed to GitHub:

```bash
git add <specific-files>
git commit -m "Short imperative summary

Optional body explaining why, not what."
git push
```

Never use `git add -A` or `git add .` — stage files explicitly. Always push after committing so GitHub stays current as the canonical save point.

## Architecture

### General Convention
Each game is a **single self-contained HTML file** — all CSS, JS, and logic inline. No external assets, libraries, or frameworks. All rendering uses the native Canvas 2D API (`fillRect`-based pixel art) or plain DOM manipulation.

---

### `shooter.html` — Retro Top-Down Shooter

Canvas: 800×600 fixed. The `<script>` block is organized into 14 numbered sections in this order:

1. **Constants & Config** — `W`, `H`, `TICK` (1/60s), `COL` palette, `STATE` enum, `LEVELS` data, `PU` power-up types
2. **Canvas setup** — precomputed checkerboard background blit each frame
3. **Input state** — `keys{}` map + `mouse` object (updated via DOM events at bottom)
4. **Utility functions** — `clamp`, `dist`, `angle`, `rnd`, `spawnEdge`
5. **Particle system** — `particles[]` array; square particles for retro feel
5b. **PowerUp class** — floats, bobs, expires after 12s, blinks when expiring
6. **Bullet class** — stores 6-position trail; separate `playerBullets` / `enemyBullets` arrays
7. **Player class** — WASD + arrow movement, mouse aim, shoot with cooldown; `activePowerup` + `powerupTimer` fields drive Rapid/Triple/Shield behavior
8. **Enemy classes** — `EnemyBase` → `Grunt` (chases + shoots), `Sniper` (stationary, lead-prediction charge shot), `Rusher` (fast, burst fires within 150px); all drop power-ups on death via `EnemyBase.die()`
9. **Wave/Level system** — `LEVELS` array drives spawn queues; `waveState`: `'spawning' → 'pausing'`; level complete triggers `STATE.LEVEL_UP`
10. **Collision detection** — AABB (`aabbOverlap`); player bullets vs enemies, enemy bullets vs player, contact damage, power-up pickup → `applyPowerup()`
11. **Renderer** — `drawHUD()`, `drawCrosshair()`, overlay functions; HUD drawn outside `ctx.save/restore` shake block
12. **Game state machine** — `gameState` switches: `MENU | PLAYING | WAVE_CLEAR | LEVEL_UP | GAME_OVER | PAUSED`
13. **Main game loop** — `requestAnimationFrame` + fixed-step accumulator; `updateGame(TICK)` called until accumulator drained, then `renderFrame()`
14. **Init + event listeners** — `initGame()` resets all arrays; DOM events at bottom wire up keyboard/mouse

**Key globals:** `player`, `enemies[]`, `powerups[]`, `playerBullets[]`, `enemyBullets[]`, `particles[]`, `score`, `gameTime`, `screenShake`, `screenFlash`, `currentLevel`, `currentWave`, `waveState`, `waveTimer`

**Power-up types** (`PU.*`): `HEALTH` (instant +40 HP), `RAPID` (8s, 35% shoot rate), `TRIPLE` (8s, 3-bullet spread), `SHIELD` (5s, full damage immunity). 30% drop chance per enemy kill.

---

### `index.html` — Tic Tac Toe

Pure DOM game. `board[9]` array tracks state; `WINS` constant lists all 8 win patterns. Score object `{ X, O, D }` persists across rounds. `checkWin()` scans `WINS` each turn. Reset clears board array and all cell classes without touching scores.
