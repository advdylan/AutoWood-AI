<table class="table is-bordered is-striped is-hoverable is-fullwidth">
                        <thead>
                          <tr>
                            <th>Marża</th>
                            <th>Koszt</th>
                            
                          </tr>
                
                        </thead>
                        <tfoot>
                          
                          <tr>
                            
                          </tr>

                        </tfoot>
                        <tbody v-if="detail_project">
                          
                            <tr>
                              <th>Marża na akcesoria</th>
                                <td>{{ detail_project.accesories_margin}}  zł   
                                </td>
                            </tr>

                            <tr>
                              <th>Marża materiałowa</th>
                              <td>{{ detail_project.elements_margin }} zł</td>
                            </tr>

                            <tr>
                              <th>Dodatkowa marża</th>
                              <td>{{ detail_project.additional_margin}} zł</td>
                            </tr>
                          
                        </tbody>
                        
                      </table>
                    </div>
                    <hr class="dashed">
                    <div class="container">
                      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                        <thead>
                          <tr>
                            <th>Dział</th>
                            <th>Koszt</th>
                            
                          </tr>
                
                        </thead>
                        <tfoot>
                          
                          <tr>
                            
                          </tr>

                        </tfoot>
                        <tbody>
                          
                          <tr v-if="detail_project" v-for="worktime in detail_project.worktimes">
            
                            <th>{{ worktime.name}}</th>
                            <td>{{ worktime.cost}} zł</td>
                          </tr>
                          
                        </tbody>
                        
                      </table>
                    </div>