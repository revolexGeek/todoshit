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
  auth: {
    isEnabled: true,
    disableServerSideAuth: false,
    baseURL: "http://127.0.0.1:8000/api/auth/",
    provider: {
      type: "local",
      token: {
        signInResponseTokenPointer: "/key",
        type: "Token",
        cookieName: "sessionid",
        headerName: "Authorization",
        maxAgeInSeconds: 1800,
        sameSiteAttribute: "lax",
      },
      endpoints: {
        signIn: { path: "login/", method: "post" },
        signOut: { path: "logout/", method: "post" },
        signUp: { path: "register/", method: "post" },
        getSession: { path: "user/", method: "get" },
      },
    },
  },
  modules: ["@nuxt/ui", "@nuxtjs/google-fonts", "@sidebase/nuxt-auth"],
  compatibilityDate: "2024-08-05",
});
