A = cell(2, 1);
A{1} = magic(2);
A{2} = magic(3);

h = cell(3, 1);
h{1} = 1;
h{2} = [0.1, 0.3; ...
    0.2, 0.4];
h{3} = [0.3, 0.2, 0.1; ...
    0.2, 0.15, 0.05];

B = cell(length(A)*length(h));

for m = 1:length(A)
    for n = 1:length(h)
        B{(m - 1)*length(h)+n} = imfilter(A{m}, h{n}, "replicate");
    end
end

for m = 1:length(B)
    disp(B{m})
    if m ~= length(B)
        disp(newline)
    end
end
