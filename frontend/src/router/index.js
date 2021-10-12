import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import BlogPost from '../views/BlogPost.vue'
import Project from '../views/Project.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
      path: '/about',
      name: 'About',
      component: About,
  },
  {
      path: '/posts/:id',
      name: 'BlogPost',
      component: BlogPost,
      props: true,
  },
  {
      path: '/projects/:id/',
      name: 'Project',
      component: Project,
      props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
