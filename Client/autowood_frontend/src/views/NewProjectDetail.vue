<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title is-centered is-size-4">Wycena zamówienia "{{ detail_project.name}}"</p>
    </header>
  <div class="columns">
    <div class="column is-half">
      
      </div>
   
    <div class="column is-half">

  </div>
</div>
</div>
   
<ElementsTable v-if="detail_project && detail_project.elements && detail_project.elements.length" :elements="detail_project.elements" />
   
    
</template>
  
  <script>
  export default {
    name: 'NewProjectDetail'
  }
  
  </script>
  
  <script setup>
  import { useProjectsListStore } from '@/store/projectslist'
  import { storeToRefs } from 'pinia'
  import { onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import ElementsTable from '@/components/ElementsTable'

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const { loadDetailProject, } = ProjectsListStore
  const {projectlist, detail_project} = storeToRefs(ProjectsListStore)
  
  
  function displayElements() {
    console.log(detail_project.value)
  } 
  
  loadDetailProject(id)

  onMounted(() => {
    loadDetailProject(id)
})




  </script>
  
  
  
  