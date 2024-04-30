<template>
    <div class="columns">
        <div class="column is-three-quarters">
            <div class="card">
                <div class="card-content">
                  <div class="content">
                    Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec
                    id elit non mi porta gravida at eget metus. Cum sociis natoque penatibus
                    et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis
                    consectetur purus sit amet fermentum.
                  </div>
                </div>
              </div>
        </div>
        <div class="column is-one-quarters">
            <div class="card">
                <div class="card-content">
                  <div class="content">
                    Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec
                    id elit non mi porta gravida at eget metus. Cum sociis natoque penatibus
                    et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis
                    consectetur purus sit amet fermentum.
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
    name: 'Project',
    data() {
        return {
            project: {},
        }
    }
}
</script>