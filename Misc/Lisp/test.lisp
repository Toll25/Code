(dex:get "http://fuperfiberneticinterpolator.challs.open.ecsc2024.it/interpolate"
         :body (drakma:encode-query-string `(("entity" . ,(format nil "application/lisp" *request-body*))))
         :content-type "application/x-www-form-urlencoded"
         :method :post)