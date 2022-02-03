function void = CalculateNb_CI_fine(outfile, nblist_CI, freq_barcodes_donor_subset, n_barcodes_observed, n_sims)

%nblist_CI = start_Nb:end_Nb;

cntr = 1;
for this_nb = nblist_CI
        r_draw_nb = mnrnd(this_nb, freq_barcodes_donor_subset, n_sims);
        for sim = 1:n_sims
            n_barcodes_transferred_nb(sim) = length(find(r_draw_nb(sim,:) > 0));
        end
        mean_barcodes_tranferred(cntr) = mean(n_barcodes_transferred_nb);
        sigma_barcodes_transferred(cntr) = sqrt(var(n_barcodes_transferred_nb));
        % might want to use Poisson or CMP distribution instead at low Nb numbers!
        prob_observed_CI(cntr) = normpdf(n_barcodes_observed, mean_barcodes_tranferred(cntr), sigma_barcodes_transferred(cntr)); % length(find(n_barcodes_tranferred_nb == n_barcodes_observed))/n_sims;
        [cntr length(nblist_CI) this_nb]
        [n_barcodes_observed mean_barcodes_tranferred(cntr) prob_observed_CI(cntr)]
    
        cntr = cntr + 1;
end

%nblist_CI
loglikelihood_CI = log(prob_observed_CI);
locs_CI = find(loglikelihood_CI > (max(loglikelihood_CI) - 1.92));
min_nb = nblist_CI(locs_CI(1));
max_nb = nblist_CI(locs_CI(end));

MLE_nb = nblist_CI(find(log(prob_observed_CI) == max(log(prob_observed_CI))))

if 0
plot(nblist_CI, loglikelihood_CI); hold on;
plot(nblist_CI, loglikelihood_CI, 'o'); 
xlabel('bottleneck size'); ylabel('log-likelihood');
ax = axis;
plot([MLE_nb MLE_nb], [ax(3) ax(4)], 'k--');
plot([min_nb min_nb], [ax(3) ax(4)], 'b--');
plot([max_nb max_nb], [ax(3) ax(4)], 'b--');
end

save(outfile, 'nblist_CI', 'loglikelihood_CI', 'MLE_nb', 'min_nb', 'max_nb');
