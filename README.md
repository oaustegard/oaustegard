# Hi 👋 I'm Oskar

Most of what's here was built with Claude, and much of it is about working with Claude: skills, memory, agent tooling and experiments that measure what the models can do. The rest is cycling, Bluesky, and whatever caught my attention that week.

## Current work

- **Muninn** — a Claude agent with persistent memory (Turso-backed), a boot sequence, and its own [blog](https://muninn.austegard.com), where it writes up the work we do together. Recent subjects: a [model advisor](https://muninn.austegard.com/blog/first-prompt-model-advisor.html) that suggests a model tier from Claude Code's first prompt, [mining 206 agent sessions](https://muninn.austegard.com/blog/mining-agent-sessions-for-broken-rules.html) for the rules it broke, and a [decision model made of Haiku](https://muninn.austegard.com/blog/a-decision-model-made-of-haiku.html). Its utilities are in [muninn-utilities](https://github.com/oaustegard/muninn-utilities).
- **Teams of small models** — how far many Haiku agents get on hard work: a [C compiler from 1,436 Haiku agents](https://muninn.austegard.com/blog/haiku-c-compiler.html), [decompiling C with 2,489 of them](https://muninn.austegard.com/blog/decompiling-c-with-haiku.html), and [getting them to act on each other's messages](https://muninn.austegard.com/blog/haiku-agent-teams.html). Code and results are in [haiku-cc](https://github.com/oaustegard/experiments/tree/main/haiku-cc), [swarm-decomp](https://github.com/oaustegard/experiments/tree/main/swarm-decomp) and [agent-mail](https://github.com/oaustegard/experiments/tree/main/agent-mail).
- **Embedding compression** — [remex](https://github.com/oaustegard/remex) (on [PyPI](https://pypi.org/project/remex/)) quantizes embeddings 4–8x and validates the result against retrieval recall. [remax](https://github.com/oaustegard/remax) does rank-correct 1-bit cosine LSH, and [remax_kb](https://github.com/oaustegard/remax_kb) packages it as a portable knowledgebase format. Results so far include a [16× smaller index for EmbeddingGemma 2](https://muninn.austegard.com/blog/sixteen-times-smaller-embeddinggemma-2-index.html) and a [plain explainer of how both compress a vector](https://muninn.austegard.com/blog/remex-remax-explainer.html).
- **Transformers as computers** — [llm-as-computer](https://github.com/oaustegard/llm-as-computer) tests Percepta's claim that attention can execute programs. [eml-sr](https://github.com/oaustegard/eml-sr) reduces the machine to one instruction, `eml(x,y) = exp(x) − ln(y)`.

## Things to use

- **[claude-skills](https://github.com/oaustegard/claude-skills)** — my collection of Claude skills: code navigation, memory, charting, media processing, Bluesky, orchestration and more, each released separately ([release index](https://austegard.com/ai-tools/claude-skill-releases.html)).
- **[austegard.com](https://austegard.com)** ([source](https://github.com/oaustegard/oaustegard.github.io)) — a static, client-side site full of tools: AI utilities, Bluesky/AT Protocol tools, web and PDF utilities, cycling tools and a few games.
- **[aeyu.io](https://aeyu.io)** ([source](https://github.com/oaustegard/aeyu.io)) — Participation Awards: recognition for efforts where effort was given.
- **[bookmarklets](https://github.com/oaustegard/bookmarklets)** — bookmarklets for Claude.ai, Strava, Bluesky and general page wrangling, with an [installer](https://austegard.com/web-utilities/bookmarklet-installer.html).
- **[browser-extensions](https://github.com/oaustegard/browser-extensions)** — Chrome/Edge extensions, mostly vibe coded: Claude usage meter, web page to Markdown, Bluesky helpers, custom redirects.
- **[claude-github-and-spoke](https://github.com/oaustegard/claude-github-and-spoke)** — a minimal template that gives Claude Code on the Web a `gh` CLI and access to your other repos.
- **[claude-sessions-mac](https://github.com/oaustegard/claude-sessions-mac)** — a macOS menu bar app that lists your Claude Code sessions and tells you when one finishes or needs you.

## Recently updated repos

<!-- BEGIN:recent-repos -->
<!-- END:recent-repos -->

## Latest from Muninn's blog

<!-- BEGIN:recent-posts -->
- [A 2-Bit Document Store for MICE-P](https://muninn.austegard.com/blog/mice-p-two-bit-document-store.html) <sub>2026-10-27</sub>
- [Self-painting SVGs from any picture](https://muninn.austegard.com/blog/self-painting-svg.html) <sub>2026-10-23</sub>
- [Clairic against Haiku 5.5 on extraction](https://muninn.austegard.com/blog/clairic-vs-haiku.html) <sub>2026-10-19</sub>
- [Planting mistakes in a subagent's memory](https://muninn.austegard.com/blog/planting-mistakes-in-a-subagents-memory.html) <sub>2026-10-16</sub>
- [Getting Haiku agents to act on each other's messages](https://muninn.austegard.com/blog/haiku-agent-teams.html) <sub>2026-10-14</sub>
- [A C compiler from 1,436 Haiku agents](https://muninn.austegard.com/blog/haiku-c-compiler.html) <sub>2026-10-13</sub>
<!-- END:recent-posts -->

<sub>Both lists refresh daily via [a GitHub Action](.github/workflows/update-readme.yml).</sub>

## Connect with me

- 🌐 [austegard.com](https://austegard.com)
- 🦋 [Bluesky](https://bsky.app/profile/austegard.com)
- 💼 [LinkedIn](https://linkedin.com/in/austegard)
- 📌 [Gists](https://gist.github.com/oaustegard)
- 🐘 [Mastodon](https://mastodon.social/@austegard) (deprecated)

## More

- [...everything else](https://www.google.com/search?q=%22oskar+austegard%22+-site%3Alinkedin.com+-site%3Atwitter.com+-site%3Agithub.com)
- [My dad, Atle Austegard](https://atle.austegard.com)
- [Other namesakes](https://www.google.com/search?q=austegard+-oskar)
