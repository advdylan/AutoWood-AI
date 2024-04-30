<template>
    <div class="columns">
        <div class="column is-full">
            <div class="card">
              <header class="card-header">
                <p class="card-header-title is-centered is-size-3">Szkic projektu</p>        
              </header>
                <div class="card-content">
                  <div class="column is-half">
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
            project: {},
        }
    }
}
</script>