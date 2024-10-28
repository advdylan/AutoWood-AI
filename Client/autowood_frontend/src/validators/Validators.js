
export function validateFormData(formData, errors) {
    if (!formData.get('name') || formData.get('name') === 'undefined' || formData.get('name').trim() === '') {
        errors.value.push('Podaj właściwą nazwę wyceny w oknie "Nazwa projektu"')
      }
      if (!formData.get('category') || formData.get('category') === 'undefined'|| formData.get('category').trim() === '') {
        errors.value.push('Podaj właściwą nazwę w oknie "Kategoria"')
      }
      if (!formData.get('wood') || formData.get('wood') === 'undefined'|| formData.get('wood').trim() === '') {
        errors.value.push('Podaj właściwą nazwę w oknie "Materiał"')
      }
      if (!formData.get('collection') || formData.get('collection') === 'undefined'|| formData.get('collection').trim() === '') {
        errors.value.push('Podaj właściwą nazwę w oknie "Kolekcja"')
      }
      if (!formData.get('paint') || formData.get('paint') === 'undefined'|| formData.get('paint').trim() === '') {
        errors.value.push('Podaj właściwą nazwę w oknie "Malowanie"')
      }

        for (let pair of formData.entries()) {
            console.log(pair[0], pair[1])
        }
}

export function validateNewAccesory(accesorytype, errors) {
  
  return 0
}