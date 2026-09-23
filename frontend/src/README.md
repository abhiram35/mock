# Frontend Source Layout

```
src/
├── api/             # Axios service modules (one per backend domain)
├── assets/          # Static images, icons, fonts
├── components/      # Reusable React components
│   ├── interview/   # Interview-specific compound components
│   ├── profile/     # Profile-specific compound components
│   └── ui/          # Generic, business-logic-free UI primitives (phase 2)
├── lib/             # Shared helpers and the central Axios instance
├── pages/           # Top-level route pages (one file per route)
│   └── admin/       # Admin-only pages
├── types/           # Shared TypeScript type definitions
├── App.tsx          # Route definitions
├── main.tsx         # React DOM entry point
└── index.css        # Global styles and Tailwind directives
```

## Conventions

- **`pages/`** compose components to build full screens; each file maps to one route.
- **`components/`** holds reusable pieces shared across pages.
- **`components/ui/`** (phase 2) will contain generic, business-logic-free
  primitives — buttons, modals, inputs, cards — that know nothing about the
  application domain. They accept data and callbacks via props only.
- **`api/`** contains one module per backend domain; each module exports
  functions that call the backend REST API via the shared Axios instance in
  `lib/api.ts`.
- **`lib/`** holds the configured Axios instance and any domain-agnostic
  utility functions.
