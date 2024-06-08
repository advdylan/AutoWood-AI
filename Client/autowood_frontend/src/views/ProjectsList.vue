<template>

    <div class="projects-list-container">
        <b-table :data="data" :columns="columns"></b-table>
    </div>

    
</template>
  

<script setup>
import { useProjectsListStore } from '@/store/projectslist'
import { storeToRefs } from 'pinia'
import Buefy from 'buefy'

const ProjectsListStore = useProjectsListStore()

const { loadProjects,} = ProjectsListStore

const { projectlist, data, columns } = storeToRefs(ProjectsListStore)


loadProjects()

</script>
  
  
  
  