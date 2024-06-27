<template>

   

    <div>
        <h1>Project Detail</h1>
        <p>Project ID: {{ id }}</p>
        <button @click="displayElements">halo</button>
        <ElementsTable :elements="detail_project.elements" />
        
        
      
    </div>  
    
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

  onMounted(() => {
    loadDetailProject(id)

})




  </script>
  
  
  
  