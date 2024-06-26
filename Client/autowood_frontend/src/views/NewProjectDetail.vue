<template>

    <button @click="loadDetailProject(18)"></button>

    <div>
        <h1>Project Detail</h1>
        <p>Project ID: {{ id }}</p>
        <!-- Add more details here based on the fetched data -->
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

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const { loadDetailProject, detail_project } = ProjectsListStore
  

  onMounted(() => {
    loadDetailProject(id)
})



  
  </script>
  
  
  
  