import { createRouter, createWebHistory } from 'vue-router'

import NewProject from '../views/NewProject.vue'
import ProjectsList from '../views/ProjectsList.vue'
import NewProjectDetail from '../views/NewProjectDetail.vue'
import PricesSetup from '@/views/PricesSetup.vue'
import Accesories from '@/views/Accesories.vue'
import Home from '@/views/Home.vue'
import NewProjectProgress from '@/views/NewProjectProgress.vue'
import CutOptimizer from '@/views/CutOptimizer.vue'


const routes = [
  
  {
    path: '/new-project',
    name: 'NewProject',
    component: NewProjectProgress,
    meta: {
      title: '| Auto-Wood |'
    }
  },
  {
    path: '/new-project-progress',
    name: 'NewProjectProgress',
    component: NewProjectProgress,
    meta: {
      title: '| Auto-Wood |'
    }
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
  },
  {
    path: '/accesories',
    name: 'Accesories',
    component: Accesories
  },
  {
    path: '/cut-optimizer',
    name: 'CutOptimizer',
    component: CutOptimizer
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: '| Auto-Wood |'
    }

  }
  
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
