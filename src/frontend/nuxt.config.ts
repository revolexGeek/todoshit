export default defineNuxtConfig({
  devtools: {
    enabled: false,
  },
  tailwindcss: {
    viewer: false,
  },
  googleFonts: {
    families: {
      Inter: {
        wght: [400, 600, 700],
      },
    },
    subsets: ["latin", "cyrillic"],
    display: "swap",
    prefetch: false,
    preconnect: false,
    preload: false,
    download: true,
    base64: false,
  },
  modules: ["@nuxt/ui", "@nuxtjs/google-fonts"],
  compatibilityDate: "2024-08-05",
});
