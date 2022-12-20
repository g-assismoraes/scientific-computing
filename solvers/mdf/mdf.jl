using JSON
using Plots

function mdf(ne, connect, cc)
    #print(ne)
    A = zeros(ne, ne)
    b = zeros(ne, 1)

    if (connect[1,1] == 1)
        aux = -2
    else 
        aux = -4
    end

    bloco = [1, 1, 1, 1]
    for e=1:ne
        if (cc[e, 1] == 0)
            A[e, e] = aux
            
            for j=2:(connect[e, 1] + 1)
                A[e, connect[e, j]] = bloco[j-1]
            end
        else
            A[e,e] = 1
            b[e, 1] = cc[e, 2]
        end
    end

    x = A \ b

    return x
end

function readJSON(_file::String)
    println(".read")
    open(_file,"r") do f
        data = JSON.parse(f)
        if  haskey(data, "connection_map") & haskey(data, "cc")

            ne = size(data["connection_map"])[1]

            connect = zeros(Int64, ne, 5)
            cc = zeros(Float64, ne, 2)

            for i=1:ne
                for j=1:5
                    connect[i,j] = convert(Int64, data["connection_map"][i][j])
                end

                for k=1:2
                    cc[i, k] = convert(Float64, data["cc"][i][k] )
                end

            end
        end
        return ne, connect, cc
    end
end


function main(filename)
    ne, connect, cc = readJSON(filename)
    y = mdf(ne, connect, cc)
    println(y)
    #l = size(x)[1]
    #x = sort(x[1:l])
    x = 1:size(y)[1]
    plot(x, y, label="MDF")
    title!("Variação de Temperatura")
    ylabel!("Temperatura °C")
    xlabel!("Pontos")
end


if length(ARGS) == 1
    main(ARGS[1])
else
    main("solvers\\mdf\\mdf.json")
end