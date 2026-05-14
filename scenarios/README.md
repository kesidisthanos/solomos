# Σενάρια Σολωμού

Ευρετήριο των σεναρίων χρήσης. Κάθε σενάριο έχει το δικό του πρωτόκολλο πριν τη σύνταξη και τα δικά του anti-patterns.

## Πώς διαλέγεις σενάριο

Η σύνταξη ή επιμέλεια ξεκινάει πάντα από επιλογή σεναρίου. Αν ο χρήστης το δηλώνει ρητά, χρησιμοποιείς αυτό. Αν όχι, διαλέγεις βάσει του τι ζητάει και του πιθανού καναλιού δημοσίευσης.

Αν κανένα δεν ταιριάζει, **δεν εφευρίσκεις σενάριο**. Πες στον χρήστη τι λείπει και πρότεινε να προστεθεί νέο αρχείο σεναρίου.

## Κατάλογος

| Κατηγορία | Αρχείο | Σκοπός | Προεπιλογή ύφους |
|---|---|---|---|
| Λεξικογραφικά / lexilog brand | [`lexilog-app-entry.md`](lexilog-app-entry.md) | Λήμμα της εφαρμογής lexilog (ορισμός, ετυμολογία, παράδειγμα) | ουδέτερο |
| Λεξικογραφικά / lexilog brand | [`lexilog-tiktok-caption.md`](lexilog-tiktok-caption.md) | TikTok caption που προωθεί λέξη + το brand lexilog | καθημερινό |
| Ακαδημαϊκά | [`high-school-essay.md`](high-school-essay.md) | Έκθεση/εργασία λυκείου | ουδέτερο |
| Ακαδημαϊκά | [`university-essay.md`](university-essay.md) | Πανεπιστημιακή εργασία/δοκίμιο | ουδέτερο |
| Επαγγελματικά | [`business-email.md`](business-email.md) | Επαγγελματικό email | ουδέτερο |
| Επαγγελματικά | [`linkedin-post.md`](linkedin-post.md) | LinkedIn post επαγγελματικού περιεχομένου | ουδέτερο |
| Επαγγελματικά | [`cv-resume.md`](cv-resume.md) | Βιογραφικό | ουδέτερο |
| Επαγγελματικά | [`cover-letter.md`](cover-letter.md) | Συνοδευτική επιστολή για αίτηση εργασίας | ουδέτερο |
| Επαγγελματικά | [`sales-or-proposal.md`](sales-or-proposal.md) | B2B πρόταση, pitch deck copy, μήνυμα συνέχειας πώλησης | ουδέτερο |
| Επαγγελματικά | [`customer-service-letter.md`](customer-service-letter.md) | Παράπονο/αίτημα προς ιδιωτική εταιρεία | ουδέτερο |
| Marketing και brand | [`marketing-copy.md`](marketing-copy.md) | Διαφημιστικό κείμενο, brand copy, headlines | καθημερινό |
| Marketing και brand | [`product-description.md`](product-description.md) | Περιγραφή προϊόντος για e-commerce | καθημερινό |
| Marketing και brand | [`press-release.md`](press-release.md) | Δελτίο τύπου | ουδέτερο |
| Marketing και brand | [`news-article.md`](news-article.md) | Άρθρο ειδήσεων ή αρθρογραφία | ουδέτερο |
| Στοχαστική γραφή | [`personal-essay-or-blog.md`](personal-essay-or-blog.md) | Στοχαστική γραφή για blog, newsletter, Substack | ουδέτερο |
| Πρακτικά / Οδηγίες | [`recipe-or-howto.md`](recipe-or-howto.md) | Συνταγή ή πρακτικές οδηγίες | καθημερινό |
| Ψηφιακό περιεχόμενο | [`app-or-ui-copy.md`](app-or-ui-copy.md) | Buttons, errors, push notifications, onboarding strings | ουδέτερο |
| Κοινωνικά μέσα και προσωπική επικοινωνία | [`social-post.md`](social-post.md) | Γενικό social media post (Facebook, X, Threads) | καθημερινό |
| Κοινωνικά μέσα και προσωπική επικοινωνία | [`instagram-caption.md`](instagram-caption.md) | Instagram caption | καθημερινό |
| Κοινωνικά μέσα και προσωπική επικοινωνία | [`whatsapp-message.md`](whatsapp-message.md) | Προσωπικά μηνύματα (WhatsApp, Viber, SMS, Messenger) | καθημερινό |
| Κοινωνικά μέσα και προσωπική επικοινωνία | [`greeting-wishes.md`](greeting-wishes.md) | Ευχές (γενέθλια, εορτές, γάμος, συλλυπητήρια) | καθημερινό |
| Προφορικός λόγος | [`speech-or-toast.md`](speech-or-toast.md) | Γραπτός λόγος για εκφώνηση (πρόποση, επικήδειος, λόγος εκδήλωσης, podcast intro) | ποικίλει |
| Επίσημα έγγραφα | [`legal-formal-letter.md`](legal-formal-letter.md) | Επίσημη επιστολή ή αίτηση σε δημόσια αρχή | επίσημο |
| Μετάφραση | [`translation-from-english.md`](translation-from-english.md) | Παραγωγή φυσικού ελληνικού από αγγλικό πρωτότυπο | εξαρτάται από αγγλικό σενάριο |

## Δομή κάθε αρχείου σεναρίου

Κάθε σενάριο τηρεί την ίδια εσωτερική δομή ώστε να φορτώνεται γρήγορα:

1. **Πότε χρησιμοποιείται**: μία πρόταση
2. **Σκοπός & κοινό**: ποιος γράφει για ποιον
3. **Προεπιλογή ύφους**: επίσημο/ουδέτερο/καθημερινό
4. **Δομή**: ποιες ενότητες/μέρη πρέπει να υπάρχουν
5. **Μήκος**: προσδοκώμενος αριθμός λέξεων ή γραμμών
6. **Πρωτόκολλο πριν το γράψιμο**: ειδικοί έλεγχοι πριν από τη σύνταξη
7. **Anti-patterns ειδικά για το σενάριο**: τι να μην κάνεις
8. **Παράδειγμα**: όπου είναι χρήσιμο
9. **Μορφή εξόδου**: πώς εμφανίζεις το αποτέλεσμα στον χρήστη

## Πώς προστίθεται νέο σενάριο

Αν εμφανιστεί συχνή ανάγκη που δεν καλύπτεται:

1. Δημιουργείς νέο αρχείο `scenarios/<scenario-name>.md` ακολουθώντας τη δομή των 9 σημείων.
2. Προσθέτεις γραμμή στον αντίστοιχο πίνακα αυτού του README.
3. Αν προκύπτουν ειδικά anti-patterns, καταγράφεις στο `patterns.yaml` με κατάλληλο `registers` ετικετάρισμα.
4. Αν είναι εφικτό, προσθέτεις τουλάχιστον ένα παράδειγμα εισόδου/εξόδου στο `few_shot.yaml`.
