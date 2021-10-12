import { createApp }  from 'vue'
import App from './App.vue'
import router from './router'

let app = createApp(App)

app.config.globalProperties.appName = 'Zack Plauché'
app.config.globalProperties.buildImageUrl = imageName => require('@/assets/images/' + imageName)

app.use(router).mount('#app')
// app.use(router).use(urlbuilder).mount('#app')