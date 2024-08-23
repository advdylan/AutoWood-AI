import {defineStore} from 'pinia'
import axios from 'axios'




export const useProjectsListStore = defineStore('projectslist', {
    state: () => ({
        projectlist: null,
        detail_project: null,

    }),
    getters: {
        data() {
            return this.projectlist ? this.projectlist.map(item => ({
                id: item.id,
                name: item.name,
                category: item.category.name,
                collection: item.collection.name,
                wood: item.wood.name,
                paints: item.paints.name,
                elements: item.elements.name,
                nawigacja: 'nawigacja'
            })) : [];
        },

        columns() {
            let columns = [
                { 
                field: 'name', 
                label: 'Nazwa',
                searchable: true
                },
                { 
                field: 'category', 
                label: 'Kategoria',
                searchable: true 
                },
                { 
                field: 'collection', 
                label: 'Kolekcja',
                searchable: true
                },
                { 
                field: 'wood', 
                label: 'Materiał',
                searchable: true 
                },
                { 
                field: 'paints',
                label: 'Malowanie',
                searchable: true 
                },
                {
                field: 'nawigacja',
                label: 'Nawigacja'
                }
            ]
            return columns
        }
    },

    actions: {

        setProjects(data) {
            this.projectlist = data

        },

        setDetaiLProject(data) {
            this.detail_project = data
        },

        async loadProjects() {
            await axios
            .get(`/api/v1/newproject`)
            .then(response => {       
                this.setProjects(response.data)
            })
            .catch(error =>{
                console.log(error)     
            })
        },

        async loadDetailProject(id) {
            await axios
            .get(`/api/v1/newproject/${id}/`)
            .then(response => {
                this.setDetaiLProject(response.data)
                console.log(`Project DETAIL ID:${id} \n ${response.data}`, response.data)
            })
            .catch(error => {
                console.log(error)
            })

        },
        async updateProject(id, editedData) {
            try {
                const response = await axios.patch(`/api/v1/newproject/${id}/`, editedData, {
                    headers: {
                        'Content-Type': 'application/json',                    
                    },
                });
                console.log('Server response:', response);
                //console.log('Project updated successfully:', response.data);
            } catch (error) {
                console.error('Error updating the project:', error);
            }
        },

        async generateReport(id) {
            axios({
                url: `/api/download-user-report/${userId}/`,
                method: 'GET',
                responseType: 'blob', // Important for downloading files
              }).then((response) => {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', `user_${userId}_report.pdf`); // or whatever the filename should be
                document.body.appendChild(link);
                link.click();
              }).catch((error) => {
                console.error("There was an error downloading the report:", error);
              });

        },

        addElement(element) {
            this.detail_project.elements.push({
              element: {
                name: element.element.name,
                dimX: element.element.dimX,
                dimY: element.element.dimY,
                dimZ: element.element.dimZ,
                wood_type: element.element.wood_type
              },
              quantity: element.quantity
            });
            console.log(this.element)
          },

        addAccesoryDetailProject(accesory) {
                
                const newAccesory = {
                    id: accesory.id,
                    project: this.detail_project.id,
                    quantity: accesory.quantity,
                    type: {
                        description: accesory.description,
                        id: accesory.id,
                        name: accesory.name,
                        price: accesory.price,
                        type: accesory.type,
                        weight: accesory.weight
                    }
                }
                this.detail_project.accessories.push(newAccesory)
            }
    },
})