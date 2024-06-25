<template>
    <div class="projects-list-container">
        <b-table :data="data">
            <template v-for="column in columns" :key="column.id">
                <b-table-column v-bind="column">
                    <template v-if="column.searchable && !column.numeric" #searchable="props">
                        <b-input
                            v-model="props.filters[props.column.field]"
                            placeholder="Wyszukaj"
                            icon="magnify"/>
                    </template>
                    <template v-slot="props">
                        <template v-if="column.field === 'nawigacja'">
                            <b-button @click="navigateToProject(props.row.id)">View</b-button>
                        </template>
                        <template v-else>
                        {{ props.row[column.field] }}
                    </template>
                </template>
                </b-table-column>
            </template>
        </b-table>
    </div>
</template>

<script setup>
import { useProjectsListStore } from '@/store/projectslist'
import { storeToRefs } from 'pinia'
import Buefy from 'buefy'

const ProjectsListStore = useProjectsListStore()

const { loadProjects } = ProjectsListStore
const { projectlist, data, columns } = storeToRefs(ProjectsListStore)

loadProjects()
</script>