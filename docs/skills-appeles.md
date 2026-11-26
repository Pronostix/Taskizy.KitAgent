# Skills appelés par les agents

Chaque agent de `agents/` a une table « Quand → skill ». Cette page en est le relevé, généré depuis les agents. Un skill du kit est recopié dans `skills/`. Un skill externe est installé à la source par `python installer.py --externes`. Un skill intégré vient de Claude Code.

## Par agent

| Agent | Skills appelés |
|---|---|
| `team-architecte` | `codex`, `design-system`, `llm-council`, `plan-eng-review`, `ultrathink` |
| `team-communication` | `brand`, `brandkit`, `cold-email`, `copywritting`, `document-generate`, `document-release`, `fix-grammar`, `linkedin-posts`, `make-pdf`, `slides` |
| `team-conseil` | `llm-council` |
| `team-cto` | `grill-me`, `last30days`, `llm-council`, `office-hours`, `plan-ceo-review` |
| `team-designer` | `app-icon`, `banner-design`, `design`, `design-consultation`, `design-review`, `design-shotgun`, `design-system`, `design-taste-frontend`, `emil-design-eng`, `high-end-visual-design`, `imagegen-frontend-mobile`, `imagegen-frontend-web`, `industrial-brutalist-ui`, `minimalist-ui`, `plan-design-review`, `redesign-existing-projects`, `slides`, `ui-ux-pro-max` |
| `team-dev-back` | `debug-code`, `fix-errors`, `investigate`, `n8n-node-configuration`, `n8n-validation-expert`, `refactor` |
| `team-dev-front` | `browse`, `clean-code`, `dev-browser`, `emil-design-eng`, `fix-errors`, `image-to-code`, `refactor`, `ui-styling` |
| `team-marketing` | `customer-research`, `landing-report`, `last30days`, `marketing`, `mom-test`, `obviously-awesome`, `offers`, `pricing`, `prospecting` |
| `team-performance` | `benchmark`, `code-simplifier`, `debug-code`, `investigate` |
| `team-product-owner` | `customer-research`, `last30days`, `mom-test`, `obviously-awesome`, `offers`, `office-hours`, `plan-ceo-review`, `pricing` |
| `team-qa` | `benchmark`, `browse`, `canary`, `debug-code`, `dev-browser`, `investigate`, `qa`, `qa-only`, `verify` |
| `team-review` | `clean-code`, `code-review`, `codex`, `devex-review`, `review`, `review-code`, `thermo-nuclear-code-quality-review` |
| `team-securite` | `careful`, `cso`, `guard` |
| `team-tech-lead` | `apex`, `brainstorm`, `plan-eng-review`, `plan-tune`, `ultrathink` |

## Par skill

| Skill | Origine | Où | Appelé par |
|---|---|---|---|
| `apex` | kit | skills/apex | `team-tech-lead` |
| `app-icon` | kit | skills/app-icon | `team-designer` |
| `banner-design` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-designer` |
| `benchmark` | externe | garrytan/gstack | `team-performance`, `team-qa` |
| `brainstorm` | kit | skills/brainstorm | `team-tech-lead` |
| `brand` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-communication` |
| `brandkit` | externe | Leonxlnx/taste-skill | `team-communication` |
| `browse` | externe | garrytan/gstack | `team-dev-front`, `team-qa` |
| `canary` | externe | garrytan/gstack | `team-qa` |
| `careful` | externe | garrytan/gstack | `team-securite` |
| `clean-code` | kit | skills/clean-code | `team-dev-front`, `team-review` |
| `code-review` | intégré | Claude Code | `team-review` |
| `code-simplifier` | intégré | Claude Code | `team-performance` |
| `codex` | externe | garrytan/gstack | `team-architecte`, `team-review` |
| `cold-email` | externe | coreyhaines31/marketingskills | `team-communication` |
| `copywritting` | kit | skills/copywritting | `team-communication` |
| `cso` | externe | garrytan/gstack | `team-securite` |
| `customer-research` | externe | coreyhaines31/marketingskills | `team-marketing`, `team-product-owner` |
| `debug-code` | kit | skills/debug-code | `team-dev-back`, `team-performance`, `team-qa` |
| `design` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-designer` |
| `design-consultation` | externe | garrytan/gstack | `team-designer` |
| `design-review` | externe | garrytan/gstack | `team-designer` |
| `design-shotgun` | externe | garrytan/gstack | `team-designer` |
| `design-system` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-architecte`, `team-designer` |
| `design-taste-frontend` | externe | Leonxlnx/taste-skill | `team-designer` |
| `dev-browser` | externe | Melvynx/ai-maxxing-skills | `team-dev-front`, `team-qa` |
| `devex-review` | externe | garrytan/gstack | `team-review` |
| `document-generate` | externe | garrytan/gstack | `team-communication` |
| `document-release` | externe | garrytan/gstack | `team-communication` |
| `emil-design-eng` | externe | emilkowalski/skill | `team-designer`, `team-dev-front` |
| `fix-errors` | kit | skills/fix-errors | `team-dev-back`, `team-dev-front` |
| `fix-grammar` | kit | skills/fix-grammar | `team-communication` |
| `grill-me` | externe | Melvynx/ai-maxxing-skills | `team-cto` |
| `guard` | externe | garrytan/gstack | `team-securite` |
| `high-end-visual-design` | externe | Leonxlnx/taste-skill | `team-designer` |
| `image-to-code` | externe | Leonxlnx/taste-skill | `team-dev-front` |
| `imagegen-frontend-mobile` | externe | Leonxlnx/taste-skill | `team-designer` |
| `imagegen-frontend-web` | externe | Leonxlnx/taste-skill | `team-designer` |
| `industrial-brutalist-ui` | externe | Leonxlnx/taste-skill | `team-designer` |
| `investigate` | externe | garrytan/gstack | `team-dev-back`, `team-performance`, `team-qa` |
| `landing-report` | externe | garrytan/gstack | `team-marketing` |
| `last30days` | externe | mvanhorn/last30days-skill | `team-cto`, `team-marketing`, `team-product-owner` |
| `linkedin-posts` | externe | kostja94/marketing-skills | `team-communication` |
| `llm-council` | kit | skills/llm-council | `team-architecte`, `team-conseil`, `team-cto` |
| `make-pdf` | externe | garrytan/gstack | `team-communication` |
| `marketing` | kit | skills/marketing | `team-marketing` |
| `minimalist-ui` | externe | Leonxlnx/taste-skill | `team-designer` |
| `mom-test` | externe | wondelai/skills | `team-marketing`, `team-product-owner` |
| `n8n-node-configuration` | externe | czlonkowski/n8n-skills | `team-dev-back` |
| `n8n-validation-expert` | externe | czlonkowski/n8n-skills | `team-dev-back` |
| `obviously-awesome` | externe | wondelai/skills | `team-marketing`, `team-product-owner` |
| `offers` | externe | coreyhaines31/marketingskills | `team-marketing`, `team-product-owner` |
| `office-hours` | externe | garrytan/gstack | `team-cto`, `team-product-owner` |
| `plan-ceo-review` | externe | garrytan/gstack | `team-cto`, `team-product-owner` |
| `plan-design-review` | externe | garrytan/gstack | `team-designer` |
| `plan-eng-review` | externe | garrytan/gstack | `team-architecte`, `team-tech-lead` |
| `plan-tune` | externe | garrytan/gstack | `team-tech-lead` |
| `pricing` | externe | coreyhaines31/marketingskills | `team-marketing`, `team-product-owner` |
| `prospecting` | externe | coreyhaines31/marketingskills | `team-marketing` |
| `qa` | externe | garrytan/gstack | `team-qa` |
| `qa-only` | externe | garrytan/gstack | `team-qa` |
| `redesign-existing-projects` | externe | Leonxlnx/taste-skill | `team-designer` |
| `refactor` | kit | skills/refactor | `team-dev-back`, `team-dev-front` |
| `review` | externe | garrytan/gstack | `team-review` |
| `review-code` | kit | skills/review-code | `team-review` |
| `slides` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-communication`, `team-designer` |
| `thermo-nuclear-code-quality-review` | kit | skills/thermo-nuclear-code-quality-review | `team-review` |
| `ui-styling` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-dev-front` |
| `ui-ux-pro-max` | externe | nextlevelbuilder/ui-ux-pro-max-skill | `team-designer` |
| `ultrathink` | kit | skills/ultrathink | `team-architecte`, `team-tech-lead` |
| `verify` | externe | Melvynx/ai-maxxing-skills | `team-qa` |

## Skills du kit que les agents n'appellent pas

`caveman`, `init-suivi`, `passation`, `point`. `init-suivi`, `passation` et `point` sont appelés par la personne (`/init-suivi`, `/passation`, `/point`). `caveman` est un mode de réponse brève que `team-conseil` demande par son nom, sans l'écrire entre accents graves dans sa table.

## Outils en ligne de commande

- `ctx7` (npx ctx7@latest) : Documentation à jour d'une bibliothèque, lancée par npx, rien à installer.
