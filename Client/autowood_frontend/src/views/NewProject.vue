<template>
    <div class="columns">
        <div class="column is-full">
            <div class="card">
              <header class="card-header">
                <p class="card-header-title is-centered is-size-3">Szkic projektu</p>        
              </header>

              <div class="columns">
              <div class="column is-half">
                <div class="card-content">               
                  <div class="content">
                    <div class="field">
                      <label class="label">Nazwa projektu</label>
                      <div class="control">
                        <input class="input" type="text" placeholder="Nazwa projektu">
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Materiał</label>
                      <div class="control">
                        <div class="select">
                          <select>
                            <option v-for="wood in project.wood"> {{ wood.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Kategoria</label>
                      <div class="control">
                        <div class="select">
                          <select>
                            <option v-for="category in project.category"> {{ category.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Kolekcja</label>
                      <div class="control">
                        <div class="select">
                          <select>
                          <option v-for="collection in project.collection"> {{ collection.name }}</option>
                          </select>
                        </div>
                      </div>
                      </div>

                      <div class="field">
                        <label class="label">Malowanie</label>
                        <div class="control">
                          <div class="select">
                            <select>
                              <option v-for="paints in project.paints">{{ paints.name}}</option>
                            </select>
                          </div>
                        </div>
                      </div>


                                       
                    </div>                 
                    </div>                                                   
                    </div>    
                    
                    
                    <div class="column">

                      <div class="card-content">               
                        <div class="content">
                      <div class="card">
                        <header class="card-header" @click="isCollapsedelements = !isCollapsedelements">
                          <p class="card-header-title">
                            Lista elementów
                          </p>
                          <a href="#collapsible-card" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
                            <span class="icon">
                              <i class="fas fa-angle-down" aria-hidden="true"></i>
                            </span>
                          </a>
                        </header>

                        

                      

           </div> 
           
           
           <div class="card">
            <header class="card-header" @click="isCollapsedpaints = !isCollapsedpaints">
              <p class="card-header-title">
                Koszty pracy
              </p>
              <a href="#collapsible-card" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
                <span class="icon">
                  <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
              </a>
            </header>
  
            <div id="collapsible-card" class="is-collapsible" v-show="isCollapsedpaints">
              <div class="card-content">
                content
                </div>
                </div>
                </div>     


                <div class="card">
                  <header class="card-header" @click="isCollapsedacc = !isCollapsedacc">
                    <p class="card-header-title">
                      Akcesoria
                    </p>
                    <a href="#collapsible-card" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
                      <span class="icon">
                        <i class="fas fa-angle-down" aria-hidden="true"></i>
                      </span>
                    </a>
                  </header>
        
                  <div id="collapsible-card" class="is-collapsible" v-show="isCollapsedacc">
                    <div class="card-content">
                      content
                      </div>
                      </div>
                      </div> 


                      
           </div> 
          </div>
        </div>
       </div>    
      </div>                          
     </div>           
    </div>

    <div v-bind:class="{'is-active': showElementModal}" id="newelement-modal" class="modal">
      <div class="modal-background"></div>
      <div class="modal-content">


        <div class="modal-card">
          <header class="modal-card-head">
                <p class="modal-card-title is-centered is-size-3">Dodaj element</p>
                <button class="delete" aria-label="close" @click="showElementModal = false"></button>        
              </header>
              
          
          <section class="modal-card-body">
            <form>

            <div class="field">
              <label class="label">Nazwa</label>
              <div class="control">
                <input class="input" type="text" placeholder="Nazwa">             
              </div>
            </div>

            <div class="field">
              <label class="label">Długość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Długość">             
              </div>
            </div>

            <div class="field">
              <label class="label">Szerokość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Szerokosć">             
              </div>
            </div>

            <div class="field">
              <label class="label">Grubość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Grubość">             
              </div>
            </div>

            <div class="field">
              <label class="label">Ilość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Ilość">             
              </div>
            </div>

            <div class="field">
              <label class="label">Materiał</label>
              <div class="control">
                <div class="select">
                  <select>
                    <option v-for="wood in project.wood"> {{ wood.name }}</option>
                  </select>
                </div>
              </div>
            </div>

            
          <footer class="modal-card-foot">
            <div class="buttons">
              <button type="submit"  class="button is-success">Zapisz</button>
              <button class="button">Anuluj</button>
            </div>
          </footer>

        </form>

      </section>

      </div>
      </div>

      <div v-for="element in elements" :key="element.id">
        <!-- Display the element data here -->
      </div>
      
    </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ElementsTable from 'src/components/ElementsTable.vue'

export default {
    name: 'NewProject',
    components: {
      ElementsTable
    },
    data() {
        return {
            showElementModal: false,
            isCollapsedacc : false,
            isCollapsedpaints : false,
            isCollapsed: false,
            isCollapsedelements: false,
            project: {},
            newElement: {
              name: '',
              dimX: 0,
              dimY: 0,
              dimZ: 0,
              wood_type: null,
              price: 0,              
            },
            elements: [],
            woods: [],
        }
    },
     mounted(){
      this.getProject()

     },
     methods: {
      async getProject() {
        await axios
        .get(`/api/v1/project/`)
        .then(response =>{
          this.project = response.data
          document.title = 'New Project | Auto-Wood'
          console.log(JSON.stringify(response.data))

        })
        .catch(error =>{
          console.log(error)
        })
      },
      addElement(){
        this.elements.push({ ...this.newElement})
        this.newElement = {
          name: '',
          dimX: 0,
          dimY: 0,
          dimZ: 0,
          wood_type: null,
          price: 0, 
        }
      }
    }
}
</script>