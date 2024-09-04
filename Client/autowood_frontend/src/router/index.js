import { createRouter, createWebHistory } from 'vue-router'

import NewProject from '../views/NewProject.vue'
import ProjectsList from '../views/ProjectsList.vue'
import NewProjectDetail from '../views/NewProjectDetail.vue'
import PricesSetup from '@/views/PricesSetup.vue'


const routes = [
  
  {
    path: '/new-project',
    name: 'NewProject',
    component: NewProject
  },

  {
    path: '/new-project/:id',
    name: 'NewProjectDetail',
    component: NewProjectDetail
  },

  {
    path: '/projects-list',
    name: 'ProjectsList',
    component: ProjectsList
  },
  {
    path: '/prices-setup',
    name: 'PriceSetup',
    component: PricesSetup
  }
  
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
