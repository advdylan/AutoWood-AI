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
                      <label class="label">Kategoria</label>
                      <div class="control">
                        <div class="select">
                          <select>

                            <option>Łóżka</option>
                            <option>Loop through categories in axios data</option>
                            
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Kolekcja</label>
                      <div class="control">
                        <div class="select">
                          <select>

                            <option>Sandemo</option>
                            <option>Loop through collection in axios data</option>
                            
                          </select>
                        </div>
                      </div>

                      <div class="field">
                        <label class="label">Malowanie</label>
                        <div class="control">
                          <div class="select">
                            <select>
  
                              <option>Naturalny</option>
                              <option>Loop through collection in axios data</option>
                              
                            </select>
                          </div>
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
                          <div class="card-content">

                            
                            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                              <thead>
                                <tr>
                                  <th>Name</th>
                                  <th>Długość</th>
                                  <th>Wysokość</th>
                                  <th>Grubość</th>
                                  <th>Materiał</th>
                                  <th>Ilość</th>
                                  <th>Cena jednostkowa</th>
                                </tr>

                              </thead>
                              
                              <tfoot>
                                <tr>
                                  <th>Podsumowanie</th>
                                </tr>
                              </tfoot>
                              <tbody>
                                <tr>
                                  <th>Nośna</th>
                                  <td>2000</td>
                                  <td>250</td>
                                  <td>25</td>
                                  <td>Buk</td>
                                  <td>2</td>
                                  <td>50</td>
                                </tr>
                              </tbody>
                              
                            </table>
                          
                            <div class="buttons">

                              <button @click="showElementModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj element</button>

                              
                              <button class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj tabelę</button>
                              <button class="button is-dark"><i class="fa-regular fa-file">&nbsp;</i>Wygeneruj rozpiskę</button>
                            </div> 

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

          </section>

          <footer class="modal-card-foot">
            <div class="buttons">
              <button class="button is-success">Zapisz</button>
              <button class="button">Anuluj</button>
            </div>
          </footer>

        

      </div>
      </div>
      
    </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'NewProject',
    data() {
        return {
            showElementModal: false,
            isCollapsedacc : false,
            isCollapsedpaints : false,
            isCollapsed: false,
            isCollapsedelements: false,
            project: {},       
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
      }
    }
}
</script>