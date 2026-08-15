#import "gost.typ": body-size, body-leading, page-margins
#import "titlepage.typ": title_page

#let report(
  title: "",
  subject: "",
  kind: "",
  author: "",
  group: "",
  university: "",
  faculty: "",
  department: "",
  city: "",
  body,
) = {
  set page(paper: "a4", margin: page-margins)
  set text(size: body-size, lang: "ru", spacing: body-leading)
  set par(justify: true)
  set heading(numbering: "1.1")
  title_page(
    title: title,
    subject: subject,
    kind: kind,
    author: author,
    group: group,
    university: university,
    faculty: faculty,
    department: department,
    city: city,
  )
  pagebreak()
  body
}
