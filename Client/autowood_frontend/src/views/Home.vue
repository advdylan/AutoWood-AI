<template>
    
    <section class="hero is-small is-primary mb-6" style="background-color: rgb(137, 168, 178);">
        <div class="hero-body">
          <p class="title">{{$t("good_morning")}} 
          </p>
          
        </div>
      </section>

      <div class="container">
      <div class="columns">
        <div class="column is-half is-offset-one-quarter">
          <div class="card">
            <header  class="card-header" style="background-color: rgb(137, 168, 178) ;">
              <p class="card-header-title is-centered is-size-4" style="color: white" >{{$t("shortcuts")}}  &nbsp;<i class="fa-solid fa-arrow-up-right-from-square"></i></p>
              
            </header>


            <div class="card-content" style="background-color: rgb(137, 168, 178) ;">
              <div class="content">
                <div class="columns">
                  <div class="column is-half">
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