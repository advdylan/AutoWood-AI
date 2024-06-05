<template>
    
</template>
  

  
<script setup>
import { useProjectsListStore } from '@/store/projectlist'
import { storeToRefs } from 'pinia'

const ProjectsListStore = useProjectsListStore()

const { loadProjects, setProjects} = ProjectsListStore



</script>
  
  
  
  