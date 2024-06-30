<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title is-centered is-size-4">Wycena zamówienia "{{ detail_project.name}}"</p>
    </header>
    <div class="card-content">

      <NewProject></NewProject>

</div>
</div>
   
   
    
</template>
  
  <script>
  export default {
    name: 'NewProjectDetail'
  }
  
  </script>
  
  <script setup>
  import { useNewProjectStoreBeta } from '@/store/newproject'
  import { useProjectsListStore } from '@/store/projectslist'
  import { storeToRefs } from 'pinia'
  import { onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import ElementsTable from '@/components/ElementsTable'
  import NewProject from './NewProject.vue'

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const elementStore = useNewProjectStoreBeta()


  const { loadDetailProject, } = ProjectsListStore
  const {projectlist, detail_project} = storeToRefs(ProjectsListStore)
  
  
  

  
  loadDetailProject(id)

  onMounted(() => {
    loadDetailProject(id)
})




  </script>
  
  
  
  