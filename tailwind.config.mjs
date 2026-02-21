/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        warm: {
          50: '#fffbeb',
          100: '#fef3c7',
          200: '#fde68a',
          300: '#fcd34d',
          400: '#fbbf24',
          500: '#f59e0b',
          600: '#d97706',
          700: '#b45309',
          800: '#92400e',
          900: '#78350f',
        },
      },
      fontFamily: {
        serif: ['Georgia', 'Cambria', '"Times New Roman"', 'Times', 'serif'],
        mono: ['"JetBrains Mono"', 'Menlo', 'Monaco', 'monospace'],
      },
      typography: {
        DEFAULT: {
          css: {
            '--tw-prose-body': '#d4d4d8',
            '--tw-prose-headings': '#fafafa',
            '--tw-prose-links': '#fbbf24',
            '--tw-prose-bold': '#fafafa',
            '--tw-prose-counters': '#a1a1aa',
            '--tw-prose-bullets': '#a1a1aa',
            '--tw-prose-hr': '#3f3f46',
            '--tw-prose-quotes': '#d4d4d8',
            '--tw-prose-quote-borders': '#d97706',
            '--tw-prose-code': '#fbbf24',
            '--tw-prose-pre-code': '#d4d4d8',
            '--tw-prose-pre-bg': '#18181b',
            '--tw-prose-th-borders': '#3f3f46',
            '--tw-prose-td-borders': '#27272a',
          },
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
