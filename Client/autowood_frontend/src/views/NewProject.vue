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

                            <table class="table">
                              <thead>
                                <tr>

                                  <th>Name</th>
                                  <th>Długość</th>
                                  <th>Wysokość</th>
                                  <th>Grubość</th>
                                  <th>Materiał</th>
                                  <th>Cena jednostkowa</th>
                                </tr>

                              </thead>
                              
                              <tfoot>
                                <tr>
                                  <th></th>
                                  <th></th>
                                  <th></th>
                                  <th></th>
                                  <th></th>
                                  <th>Podsumowanie</th>
                                </tr>
                              </tfoot>





                            </table>




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
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'NewProject',
    data() {
        return {
            isCollapsed: false,
            isCollapsedelements: false,
            project: {
              items: []
            }
            
        }
    }
}
</script>