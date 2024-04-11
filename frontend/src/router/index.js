import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateQuizView from '../views/CreateQuizView.vue'
import QuizView from '../views/QuizView.vue'
import NotFound from '../views/NotFound.vue'

const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/create',
    component: CreateQuizView
  },
  {
    path: '/quiz/:id',
    component: QuizView
  },
  {
    path: '/:catchAll(.*)',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router
