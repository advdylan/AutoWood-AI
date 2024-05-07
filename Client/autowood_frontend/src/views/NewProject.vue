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
                            <option v-for="wood in wood"> {{ wood.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Kategoria</label>
                      <div class="control">
                        <div class="select">
                          <select>
                            <option v-for="category in category"> {{ category.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Kolekcja</label>
                      <div class="control">
                        <div class="select">
                          <select>
                          <option v-for="collection in collection"> {{ collection.name }}</option>
                          </select>
                        </div>
                      </div>
                      </div>

                      <div class="field">
                        <label class="label">Malowanie</label>
                        <div class="control">
                          <div class="select">
                            <select>
                              <option v-for="paints in paints">{{ paints.name}}</option>
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

                        <div id="collapsible-card" class="is-collapsible" v-show="isCollapsedelements">
                        <div class="card-content"></div>

                        <ElementsTable/>

                        <div class="buttons">

                          <button @click="showElementModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj element</button>

                         
                          <button class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj tabelę</button>
                          <button class="button is-dark"><i class="fa-regular fa-file">&nbsp;</i>Wygeneruj rozpiskę</button>
                        </div>
                        </div>

                    

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
            <form @submit.prevent="addElement">

            <div class="field">
              <label class="label">Nazwa</label>
              <div class="control">
                <input class="input" type="text" placeholder="Nazwa" v-model="newElement.name" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Długość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Długość" v-model="newElement.dimX" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Szerokość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Szerokosć" v-model="newElement.dimY" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Grubość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Grubość" v-model="newElement.dimZ">             
              </div>
            </div>

            <div class="field">
              <label class="label">Ilość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Ilość" v-model="newElement.quantity" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Materiał</label>
              <div class="control">
                <div class="select">
                  <select v-model="newElement.wood_type">
                    <option v-for="wood in wood"> {{ wood.name}}</option >
                  </select>
                </div>
              </div>
            </div>

            
          <footer class="modal-card-foot">
            <div class="buttons">
              <button @click="elements.addElements()" type="submit"  class="button is-success">Zapisz</button>
              <button class="button">Anuluj</button>
            </div>
          </footer>

        </form>

      </section>

      </div>
      </div>


    </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ElementsTable from '@/components/ElementsTable'
import { mapState } from 'vuex'

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
            newElement:  {
              name: '',
              dimX: '',
              dimY: '',
              dimZ: '',
              quantity: '',
              wood_type: ''
            }

            
            
        }
    },
    computed: mapState([
      'category',
      'worktimetype',
      'accesorytype',
      'wood',
      'collection',
      'paints',
      'elements'
      
    ]),
      
     mounted(){
     },
     created(){
      this.$store.dispatch('loadData')   
     },
     methods: {      
      addElement() {
        this.newElement = {
        name: '',
        dimX: '',
        dimY: '',
        dimZ: '',
        quantity: '',
        wood_type: ''
  }
        console.log(this.newElement)
        this.$store.commit('addElement', this.newElement)
  
  
}

            
  
}
    }

</script>
