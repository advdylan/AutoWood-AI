<template>
    
    <section class="hero is-small is-primary mb-6" style="background-color: rgb(90, 120, 90);">
        <div class="hero-body">
          <p class="title">{{$t("good_morning")}} 
          </p>
          
        </div>
      </section>

     
      <div class="columns">
        <div class="column is-one-fifth">
          <div class="card">
            <header  class="card-header" style="background-color: rgb(192 210 192) ;">
              <p class="card-header-title is-centered is-size-4"  > Narzędzia  &nbsp;<i class="fa-regular fa-file-lines"></i></p>          
            </header>
            <div class="card-content" style="background-color: rgb(192 210 192) ;">
              <div class="content">
                <div class="columns">
                  <div class="column is-full">
                  
                  <button class="button is-success is-light" style="width: 100%; margin: 1%;">Szybka wycena &nbsp;<i class="fa-solid fa-coins"></i></button>
                  <button class="button is-success is-light" style="width: 100% ; margin: 1%;">Szybka wycena &nbsp;<i class="fa-solid fa-coins"></i></button>
                  <button class="button is-success is-light" style="width: 100%; margin: 1%; ">Szybka wycena &nbsp;<i class="fa-solid fa-coins"></i></button>
                  </div>

                </div>
                  
                 
                </div>
                
       
            </div>
          </div>




        </div>
        <div class="column is-half is-offset-one-fifth">
          <div class="card">
            <header  class="card-header" style="background-color: rgb(192 210 192) ;">
              <p class="card-header-title is-centered is-size-4"  >{{$t("shortcuts")}}  &nbsp;<i class="fa-solid fa-arrow-up-right-from-square"></i></p>          
            </header>
            <div class="card-content" style="background-color: rgb(192 210 192) ;">
              <div class="content">
                <div class="columns">
                  <div class="column is-half ">
                    <div class="container">
                      <ul class="is-size-5">
                        <li class="is-size-5">
                          <router-link to="/projects-list">{{$t("projects_list_and_estimates")}} </router-link>
                        </li>
                        <li >
                          <router-link to="/new-project">{{$t("new_estimate")}}</router-link>
                        </li>
                      </ul>
                    </div>

                  </div>
                  <div class="column is-half">
                    <div class="container">
                      <ul class="is-size-5">
                        
                        <li >
                          <router-link to="/accesories">{{$t("manage_accessories")}}</router-link>
                        </li>
                        <li >
                          <router-link to="/prices-setup">{{$t("manage_labor_costs")}}</router-link>
                        </li>
                      </ul>
                    </div>

                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    
</template>

<script setup>

</script>

<style>



.card {
  --bulma-card-radius: 0.3rem;
}

a{
  color: #0333b4;
}
</style>