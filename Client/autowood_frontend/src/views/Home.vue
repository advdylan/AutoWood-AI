<template>
    
    <section class="hero is-small is-primary mb-6" style="background-color: rgb(242, 248, 254);">
        <div class="hero-body">
          <p class="title" style="color: rgb(120, 157, 188);">{{$t("good_morning")}} 
          </p>
          
        </div>
      </section>

      <div class="container">
      <div class="columns">
        <div class="column is-half is-offset-one-quarter">
          <div class="card">
            <header  class="card-header" style="background-color: rgb(242, 248, 254) ;">
              <p class="card-header-title is-centered is-size-4" style="color: rgb(120, 157, 188);">{{$t("shortcuts")}}  &nbsp;<i class="fa-solid fa-arrow-up-right-from-square"></i></p>
              
            </header>


            <div class="card-content" style="background-color: rgb(242, 248, 254) ;">
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
:root {
  --bulma-scheme-main: rgb(230, 240, 247);
  --bulma-background: rgb(230, 240, 247);
  --bulma-scheme-main-l: rgb(230, 240, 247);
  --bulma-input-placeholder-color: black;
}
.input::placeholder {
  color: var(--bulma-input-placeholder-color);
}
.input {
  background-color: rgb(243, 248, 252);
}



.card {
  --bulma-card-radius: 0.3rem;
}

a{
  color: #0333b4;
}
</style>