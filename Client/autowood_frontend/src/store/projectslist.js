import {defineStore} from 'pinia'
import axios from 'axios'
import { useLink } from 'vue-router';




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

/*     linkFiles(){
        for (let img of this.detail_project.image){
            return 0
        } */

    

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
                //console.log('Server response:', response);
                //console.log('Project updated successfully:', response.data);
            } catch (error) {
                console.error('Error updating the project:', error);
            }
        },

        async downloadElementsTable(id) {
            axios({
                url: `/api/v1/newproject/elements-production/${id}`,
                method: 'GET',
                responseType: 'json',  // Expect JSON response
            })
            .then((response) => {
                // Check if the response includes the path to the generated PDF
                if (response.data && response.data.path) {
                    const filePath = response.data.path;
        
                    // Make a second request to download the file as a PDF
                    axios({
                        url: filePath,
                        method: 'GET',
                        responseType: 'blob',
                    })
                    .then((fileResponse) => {
                        const href = URL.createObjectURL(fileResponse.data);
                        const link = document.createElement('a');
                        link.href = href;
                        link.setAttribute('download', `rozpiska_produkcja_${id}.pdf`);
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);
                        URL.revokeObjectURL(href);
                    })
                    .catch(error => {
                        console.error("There was an error downloading the file", error);
                    });
                } else {
                    console.error("File path not found in response");
                }
            })
            .catch(error => {
                console.error("There was an error fetching the file path", error);
            });
        },
        async downloadPriceReport(id) {
            axios({
                url: `/api/v1/newproject/pricing-report/${id}`,
                method: 'GET',
                responseType: 'blob',
                headers: {
                    'Accept': 'application/pdf',
                    // 'Authorization': `Bearer ${token}`,  // Uncomment if your API requires a token
                }
            })
            .then((response) => {
                console.log(response)
                const href = URL.createObjectURL(response.data)

                const link = document.createElement('a')
                link.href = href
                link.setAttribute('download', `raport_wycena_${id}.pdf`)
                document.body.appendChild(link)
                link.click()

                document.body.removeChild(link)
                URL.revokeObjectURL(href)
                
            })
            .catch(error => {
                console.log("There was an error downloading the file", error)
            }) 
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