import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import "@vuepic/vue-datepicker/dist/main.css";

const app = createApp(App);

app.use(createPinia());

app.mount("#app");
