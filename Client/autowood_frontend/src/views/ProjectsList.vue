<template>

    <h1>HALO</h1>
    
</template>
  

  
<script setup>
import { useProjectsListStore } from '@/store/projectslist'
import { storeToRefs } from 'pinia'

const ProjectsListStore = useProjectsListStore()

const { loadProjects,} = ProjectsListStore

loadProjects()




</script>
  
  
  
  