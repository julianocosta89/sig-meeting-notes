SIG: Packaging SIG
Date: 2026-05-20
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Denys Sedchenko 00:01:33 Hi, how are you?
Michele Mancioppi 00:01:37 Hiya.
I think Antoine cannot make it today, he's double booked.
I don't know if somebody else will… Join, so let's wait a couple of minutes.
Hmm.
There's a whole bunch of people that said that they wanted maintainership on the ship, but they are not joining.
Which is not great.
Now, let's get started.
So, let me open the, repository and issues.
We've got a couple of PRs merged this week, to, oh, hi, Ted!
Ted Young 00:03:19 Ayy, how's it going?
Michele Mancioppi 00:03:22 We were wondering if somebody else would join the, Today, Antoine is, is out.
I was wondering who else of the, the maintainers would, would join, but… We'll get started, meanwhile.
So, we merged a couple of PRs for the, the list of maintainers, which is everybody who signed up in the, staff wanted section of the project.
As per policy, I understand.
And, our first version of the scope, this is also out of the project.
The last time we met, last week, we created, the first, three issues.
For getting started.
One was investigating the package hosting options, and, Denise Has went, has gone.
And looked into that, and then we'll look into it in the details now.
I took the validating of the meta package architecture, so the different packages and how they relate with each other.
And, I, went and fleshed out a document for that, because I realized that some of the stuff that I had in my head never made it in the POC, that, is in the injector code, and I also found a couple of things, and, Jack and, and a couple of other people have been commenting, and I have some homeworks to do in fixing the stuff.
The last time we spoke, we realized that Aware, the kind of system where we host the packages, has implications on how we build them.
Some of the hosting is, has integrated stuff, and there is different options in terms of signing of the packages, whether we have controls of the keys or not, which is usually a great idea.
What about SSL certificates?
And, whether we can point it through with a CNAME. This is important going forward, because while the hosting may change over time.
Ideally, the SSL certificate and the CNAME would not. That is a very disruptive change for end users when the URL for a package system changes, and a lot of people set it up once, never again, and they stop getting updates.
Which is not great, especially in case of security updates.
Yeah, so maybe, Denise, you want to bring us through your findings?
Denys Sedchenko 00:06:07 Okay.
So, I was looking, like, on different available options besides wholesale hosting strategy.
So, the first option that was mentioned on a previous meeting was OBS.
So, and also Pinsuser provides a self-hosting option, so I can, like.
make self-hosting… self-hosted, or basically use a public instance of OBS from OpenSUSE, I checked who is actually using it. Podman is, by the way, all the links clickable. All the links basically pointing to the repos of the project that I mentioned. The first one is basically Podman, which has a… Which builds packages and have repos for different… Linux distros.
Also, I saw repos of different Linux distributions also built there, and also Kubernetes.
I was surprised at Kubernetes is using it in it. I also attached a link with his announcement of Kubernetes actually moving to there, but Kubernetes is using it basically partially, so they use it to basically build packages, sign packages, prepare Repositories, information, But… As I understand, OBS will not be able to basically handle all of the traffic, incoming traffic, plus it does not support CNAME.
So they basically deploy those… these three metadata and packages to a separate bucket.
Plus, they have, they have, basically, a load balancer in front of it. Like, when you go to pkgs.kubernetes.io, it redirects you… load balancer redirects you to S3 bucket, and then you get your, basically, fact packages from there.
So, the OBS, like, we have a cloud version, like, technically it's, like, Most like a shared instance.
Also, it provides you runners to build packages for different architectures and Linux distros, for example, exotic architectures like PowerPC, for example. It supports signing both packages and also the repo metadata, but you have to… Manage, basically, rotate and manage keys yourself.
By the way, I saw, like, on all the options I saw, like, that you have to basically still manage keys yourself.
The second option is a service called Cloudsmith.
from what I understand, it's basically a… it's a distribution service, which allows you, basically.
to create repos for different distros. They provide CDN, they provide an option to have custom domains.
And also, you can sign packages.
But they don't provide any kind of builders, any kind of CI. You have to basically upload packages yourself.
They have an open source.
Michele Mancioppi 00:09:18 What is the point of… what is the point of… Having a system that doesn't build, but can sign.
Denys Sedchenko 00:09:25 Basically, they sign repository metadata for you.
Michele Mancioppi 00:09:30 Alright.
Denys Sedchenko 00:09:33 They have an open source program.
Some projects are using it, and also they have 40 days trial.
So… The third option is similar to the previous one.
is packagecloud.io, It's similar to Cloudsmith.
Have open source program, have custom domains, have CDN, But they also only sign rep permitted data, you have to sign packages yourself. By the way, regarding CloudSmith, it's not really clear.
whether ALSO packages are signed or not.
So, I just… so, like, the concern about signing packages is included only for Package Cloud.
Michele Mancioppi 00:10:22 If you're uploading the packages, I assume that they need to be already pre-signed.
Denys Sedchenko 00:10:29 it was not really clear… it wasn't clear for me in CloudSmute documentation, but for Package Cloud, it was, like, clearly stated.
Also, no CI… Just, basically, storage and distribution.
And the last option… is GitHub Actions, plus your CDN and your blob storage. You basically build and sign packages yourself, and build repo metadata in your CI.
And then we can take something like Cloudflare Stack with Cloudflare CDN and Cloudflare Bob Storage.
So, like, we upload packages to blob storage, CDN basically forwards to it, and plus Cloudflare already provides you the SSL certificate out of the box.
So we don't need to deal with Let's Encrypt.
And also, they provide caching.
Michele Mancioppi 00:11:18 Yeah, but then it's, if we migrate up a Cloudflare, then it's a completely different certificate.
Different signature, probably different CA, which means that the portability of that, it doesn't exist.
Denys Sedchenko 00:11:33 Mmm… From my own projects, when I initially had Let's Encrypt and then switched to Cloudflare, I don't remember having, like, signature problems.
And also, Cloudflare has a project at Alexandria, which is also, like, sponsorship of those projects.
God flare was just provided as an example.
But we can take, Amazon, for example.
which have CloudFront, and also have S3. This is what Kubernetes use.
Ted Young 00:12:04 There's also, F5 is directly involved in OpenTelemetry.
So they work on OpenTelemetry and use it?
They also provide, I think, most of these services.
Denys Sedchenko 00:12:23 Yeah, so basically…
Michele Mancioppi 00:12:24 This is the basic.
Denys Sedchenko 00:12:26 overview.
Michele Mancioppi 00:12:28 I would be quite scared of the do-it-yourself.
Especially now.
It's, it's gonna take… I mean, doing something that barely works is enough.
Doing something that is secure, that you don't leak keys.
That's not easy.
That requires effort.
Denys Sedchenko 00:12:51 If you want to avoid, basically.
In my opinion, both, like, the best case, like, the best scenario out of… for provided is probably what Kubernetes did, where they basically, they have a build and signature process on, like, OBS part, and then you basically upload it to the CDN.
If you're open to more ideas, please let me know.
Michele Mancioppi 00:13:19 No, I do like the, the idea of having the building infrastructure and signing somewhere else, that the hosting is not a difficult bit.
The, the part that would scare me is the signing. They're just putting an S3 bucket behind the cloud front.
Pine.
That's fine.
Denys Sedchenko 00:13:40 Please let, Elso… Among all of the options, the key rotation… Like… is still… should… will be on us, even with OBS.
Michele Mancioppi 00:13:52 Yes.
Denys Sedchenko 00:13:52 It can be signing, but rotation is on our side.
So we need some, like, separate, like, place to store keys and probably rotate them.
Michele Mancioppi 00:14:03 No, I mean, rotating a PGP key, then that would invalidate the, I mean, the first time that you connect to an EPT repository, you offset the key. That's true. The moment you rotate those keys, all the configurations that exist out there, they no longer work.
Denys Sedchenko 00:14:21 That's true, but, like… Most of the keys, they have a TTL.
Michele Mancioppi 00:14:29 Fair.
Ted Young 00:14:32 It feels like maybe a question we want to get the security SIG and the TC involved in.
Michele Mancioppi 00:14:39 Yep.
Ted Young 00:14:40 Like, we can propose a solution to the community, and then be like, how should we deal with keys?
Michele Mancioppi 00:14:50 I mean, it would be lovely to be able to share the infrastructure of Kubernetes, to piggyback on that.
Yeah. That would be lovely.
Because, I mean, they must have hardened it by now.
So you could just take it and make another deployment of that?
Who's the… with whom we need to talk for that?
Denys Sedchenko 00:15:18 Oh, to be honest, I was trying to sign up on OpenSUSE to just create a scratch, repo on OBS, I was managing to sign in, sign up.
Sign up is done on a separate portal, but I wasn't able to sign in.
I would try to research again, like, maybe I missed something, I just, like, I registered.
Anikla tried to sign in and it didn't work, saying, like, the password is invalid. I tried to reset the password multiple times, it didn't work.
Maybe we need some kind of invitation to get there.
Michele Mancioppi 00:15:54 Hmm.
Ted Young 00:15:57 It would be worth… checking in with Kubernetes also to make sure they're happy with the choice that they made.
Denys Sedchenko 00:16:06 What is the best place to… contact them, like, we have the same CNC of Slack.
Ted Young 00:16:18 I think it would be to find the right SIG within Kubernetes, but we could just start with a more generic place and ask.
Where'd it go from there?
Actually, I take it… they have their own Slack, maybe.
Michele Mancioppi 00:16:39 What happened with, with the migration off of Slack?
That was sandboxed, and we're not doing it again anymore.
There was an entire Brumaja last year.
Ted Young 00:16:50 Oh, yeah, no, that Slack changed course.
Because they had, like, canceled their OSS program, basically. But then realized that was dumb.
Michele Mancioppi 00:17:06 I was not super smart, huh?
Ted Young 00:17:08 Yeah.
So, no migration, thankfully.
Denys Sedchenko 00:17:13 Okay, I'll search some points of context with Kubernetes, and… I will… Append their feedback to the ticket.
Michele Mancioppi 00:17:27 Yes.
Denys Sedchenko 00:17:29 By the way, on the previous… on the first sick call, I guess… Was, someone mentioned that… a different SIG has some sign, key signing already infrastructure established.
Michele Mancioppi 00:17:43 That is the collector. The collector has, key signing for the DBN and RPM packages for the collector.
And, the idea was to go and ask them.
How they like it.
For example, a good personal contact, I think, would be Alex Bolton, very likely.
Ted Young 00:18:02 Yeah.
We should definitely be doing the same thing as them.
I mean, if they're happy with that, do that. If they aren't… Mike… help them migrate to whatever the new thing is.
Michele Mancioppi 00:18:14 I mean, I also have the wish to bring the collector packages into the fold of these system packages, so much more the reason to do something similar. They never felt the need, apparently, of having an APT repository or a YAM repository as always one single package.
So, that infrastructure is missing for them.
Denys Sedchenko 00:18:37 It's Alex Bolton, right?
Michele Mancioppi 00:18:39 That's both hands.
Denys Sedchenko 00:18:41 Okay.
Ted Young 00:18:42 But you could also ask in just the collector channel, you know, collector dev.
Denys Sedchenko 00:18:48 Okay?
Michele Mancioppi 00:18:55 Alright, so maybe we pivot.
to the bits about the meta architecture.
So there are, meta architecture is how the different packages are going to relate to one another.
why, the moment you do APT install, open telemetry, all the rest of the stuff gets pulled in.
And, something that is non-trivial.
Is how to make it in a way that is future compatible.
Something that, for example, I didn't get right the first time around I wrote a proposal is thinking about interface IDs.
This number here, the appendix, like this number 1 on the end, is not.
a package version.
This is an interface version.
For example, when you go and install an SSL library.
You're usually gonna use LEAP SSL3.
What does the 3 stand for? It's not the SSL 3.0, it is the first revision of the contract of the package.
It, sometimes it's because the API changes in backwards, incompatible ways, but in our case.
We would increase that number when something profound changes in the way that the packages interact with one another.
For example. Today, the, The unspoken contract between the injector and the languages is that the moment a file, the files with the SDK packages exists on the file system, and it's reachable from the process, and the process environment is changed in just the right way, then the SDK is injected.
which SDKs are available to inject?
Where are the… where they're located are configuration files in the interactor.
And it is something that the current design has a conf-ty approach, so you have a directory in HTCD where, the different language packages are going to add their files.
And the injector will go and look for them. The moment you decide to change, for example, that configuration mechanism, the moment we move the folder, the moment the injector somehow discovers it in a different way.
That would cause a break in the way that The injector expats the language packages to behave, and we would increase This number here.
Since there is a number here, the, For example, this is a virtual dependency, there is not going to be any package in the repository that actually has this name.
But, for example, the community Java package and the text little Java package, whatever, they're going to say that they satisfy this dependency.
So this is a virtual package, there is no package like this.
But it says, I'm looking for something that will work as a paternal instrumentation, Let's take this one.
The rest is a lot of details around it. This was, this bit was the biggest piece I was missing, I think.
I cannot guarantee that I'm not missing something else.
I will try to get some former colleagues at Canonical to go through it, to say, in case I missed something. It would be great to have some Red Hatter.
look at it as well, because I am comfortable with the APT.
Package ecosystem, RPM Lasso.
There was a bunch of, a bunch of comments. One, for example, Jack is asking, very solid questions, to which I do not have yet answers in terms of what is the versioning policy of the actual packages themselves. So, when there is the, the Java package.
What is its version number?
In Java, one valid answer would be to say the version of the Java agent inside.
That does not apply to literally any other… language, because the content of the packages is a collation of 30 different artifacts with completely different versioning schemes. And even if the versioning scheme is the same, like packages in Contrib.
It's not always the case that Contrib for Python releases the packages all the time. If there are no changes, no new package is released.
So there, I, do not know what the versioning scheme should be.
I would like to keep it separate from this, from this design document. The version scheme, I think, deserves a dedicated document.
So… That's it.
If I recall correctly, versioning is a topic in stable by default, right?
Ted Young 00:25:59 Yeah, I mean, this… certainly, packaging is one of the… work streams.
Because this involves… all the different SIGs.
So…
Michele Mancioppi 00:26:12 I meant, I meant versioning.
So today, different language stakes, they do… Rather random things, as far as I can tell.
Ted Young 00:26:22 Right. So, I think the degree to which, you know, that we're talking about packaging.
As more than just this SIG, right? There's the work we can do, you know, just as a group on our own, and then there's, you know, discussions we need to have with all the maintainers and changes we maybe need to see. So, I think the best thing there is for us to… You know, package that up as, like, a presentation of, like.
what are the different things we're seeing, or at least some examples, and some proposal around, like, what we would need to see to make packaging work? I think, you know, you were saying it's… mostly just everything conforming to Senver, right? But… one of the things that SIG needs to do is, is kind of, like, Help… Those maintainers by auditing what they're already doing, and… Coming back to them with a proposal.
Michele Mancioppi 00:27:26 I'll take this one.
Okay, so at the moment, for example, T, I do not believe we need to… to land on a… on a stable versioning scheme.
For, for having the first version of the system packages out.
Ted Young 00:27:47 Yeah.
I've also wondered about, like, what kind of weird edge cases are there? For example, you know, you've got… Different versions of instrumentation, but you've got, like, different target versions.
as well, right? Like, you've got… you have a framework, right? And you might have, like, maybe these just end up being different instrumentation packages, right? But… I don't know to what degree we're in situations where you have version 4 of a framework, and then you have version 5 of a framework, and the instrumentation for those things are different.
Michele Mancioppi 00:28:27 Oh, it's very common. For example, when you look at Java, that happens all the time.
Ted Young 00:28:31 Right. But I don't know how much, moving to, like, a packaging version of this versus using the language's dependency manager to resolve everything.
you know…
Michele Mancioppi 00:28:42 No, it's not… it's not… we don't… we don't need that. It's… it's a matter of how our instrumentations are installed.
Right. So, when you go and look at, on… Ted, what's your favorite language? I can do it in any language.
Ted Young 00:28:56 Ruby.
Michele Mancioppi 00:28:58 Oh, you're challenging me.
So this is mostly an instrumentation thing, so I'll go for a contrib… For example, MySQL 2… no, this is actually a Ruby Gem.
That's… yeah.
I mean, what do we have for real? Who's not really doing that.
Ted Young 00:29:22 Yeah.
Michele Mancioppi 00:29:23 Let's go and grab, Let's go and grab trouble. It's the one where it's, it happens a lot, because the… the… sorry, Denise?
Denys Sedchenko 00:29:34 Yeah, I have a question about versioning. So, we have basically a version of Target, Version of the contract.
But we also have a version of the package. Let's assume we published… A bug… like, the buggy package or package needs to be updated, but for the same version of SDK or a framework.
How this, like…
Michele Mancioppi 00:29:58 So, in that case, what happens is that, and this is what we're looking… Into it for now.
I'm looking for a good example of this, where there are I need something where we support multiple versions, so probably Apache Client.
There we go. So, here, when there are major changes in the… well, API is the wrong word, but stick with me. Like, the shape of the API, or shape of the internals, sometimes it is like that.
you end up creating different versions of the instrumentation, and then at runtime, the SDK and the auto-instrumentation facilities decide which one to apply. And we will ship all of them.
Ted Young 00:30:46 Great. So that's, like, the fact that they're published as different, packages is what gets around that.
Michele Mancioppi 00:30:54 Yeah, but it's not always packaged, for example, that, In Java, for example, Java, it's one package. It's one JAR file that contains all of them. In, In other situations, you may have separate packages. I'm not aware… I've seen it done in other… in proprietary code. I've not seen it in OpenTelemetry where you really need to add a different package altogether.
To make it work, but it is theoretically possible that we end up having multiple NPM packages.
for technically the same library and framework, but then, at runtime, when it goes and activates, it goes… let's say, for example, in Node.js, the, the instrumentation is done up front, so the loading Goes and tries to require the packages.
Because you need to effectively wrap around them, that's what Node.js instrumentations do, they're closures. Then it goes and looks at the shape of the prototypes, so the type system on Node.js, and if it finds the right fields and methods, I say, okay, I'm active. Otherwise, it says, nope.
And it's gone. And this kind of the… It's not really clear-cut where the package begins or not, it's more like it's… it's better to think about it as instrumentation versions, and the language-specific packages they're shipped as is pretty orthogonal.
Ted Young 00:32:25 Yeah, yeah, I think… I guess what I'm saying is, like, in a world where… and maybe it's not the target language, I think the… The other place we've proposed giving people options is, like, and maybe this isn't realistic, but, like, which version of the… semantic conventions are omitted, like… you know.
I don't know how realistic that is to try to give to people.
it's certainly not something we're trying to do at all right now.
Michele Mancioppi 00:32:58 And even then, that would be another orthogonal thing from instrumentation, because then the instrumentation needs to implement all of the supported ones, yeah?
Ted Young 00:33:06 Right.
Michele Mancioppi 00:33:07 Based on configuration, which one to emit.
Ted Young 00:33:09 it… that's just… the thing I'm noticing is, like, there's… I've seen some aspirational things that mean, like, offering things on multiple axes, right? Where you… you can't just do that with a single version number, you know? Like, it gets confusing. So maybe this… the answer is, like, those things are just aspirational, and we can't realistically… Offer them to people, or they have to be offered as, like.
Something going on in the code.
Michele Mancioppi 00:33:35 I do not believe for a second that it makes sense to split For example, a different DBM package per Node.js, other instrumentation.
That makes, like, zero sense. Absolutely zero.
The… we're going to call… even just making it actually work with version ranges, freaking impossible.
So that is, in my head, the no-doubt instrumentation is one single thing, and then, for example, the activation and deactivation of instrumentations, that is why I'm so dead set about all the systems based on declarative config.
Because it is setting up what you want to turn on and off, that is what the character config is really good at.
So, it's gonna be a monolithic Node.js package, and then if there is something that you don't want it to run, then you turn it off.
Ted Young 00:34:22 I think that makes plenty, plenty of sense. I don't think we're actively hearing from people who are complaining about bits getting downloaded that they aren't planning on using, or wanting to make custom packages. But that's certainly not something we have to worry about in the first iteration of this.
Michele Mancioppi 00:34:42 So ideally, the moment we have a decent idea about the hosting.
We can pivot into making a first, first version.
To, to give people to try.
It's like…
Ted Young 00:34:56 Yeah.
Michele Mancioppi 00:34:57 It's something, for example, I would love to have a slot at Observability Day in the maintainer track to show what we're doing there.
Antoine, also, had the idea of, submitting a KubeCon.
Talk about the, system packages, and what it means in terms of operations.
Ted Young 00:35:22 Yep.
They definitely, you know, I was talking to, to Chris.
at CNCF, you know, they're very excited for us to graduate, and they're looking for what are, you know, thinking outside the box, what are different ways to… to help promote the project.
you know, other than just announcing it in the keynote and, like, having a party or something. So there's definitely opportunities, especially at the next set of upcoming KubeCons, like, KubeCon… japan I'm gonna be at, then NA, and then EU. NA and EU being the big ones, like… what can we do? I think the more we come in with a roadmap and a plan, and a, like, this is, like.
Trying to present this stuff is bigger than just being a bunch of random sigs working on stuff.
they're willing to give us some space, but I certainly think that the most obvious thing is just, like, yeah, apply for a talk, or something like that. But if for some reason we aren't getting the talk space that we need.
I think we can find other places to… To be discussing this.
one way I want to promote what we're doing with the system packaging is, you know, we're talking about, like, running in production, but I think this is also the new kick-the-tires day-to approach for OpenTelemetry. We kind of want to rewrite all of our docs on, like, getting started and trying OTEL out to be much more just… You know, go install this package and then play with it.
And so that's a big change we wanna… we want to really… once we've got that working, really promoting that hard out there in the community, I think is gonna make a big difference in terms of OpenTelemetry adoption, so…
Michele Mancioppi 00:37:20 We need to go and talk to Severin.
Ted Young 00:37:22 Yeah. Yep. Coms and docs, but then making sure we're able to kind of, like, promote it at… the CNCF, and, you know, some things we've gotten in the past are, like, I forget what they call their hands-on labs.
Michele Mancioppi 00:37:40 Right, but…
Ted Young 00:37:41 they have, like, workshops and stuff, and it's more just, like, sometimes we get a workshop, sometimes they give the workshops to other projects, and if we can just make sure that we have a workshop at… at NA and EU, and that we're using that workshop time to, like, just get people going, you know, with OTEL for the first time, and we have this stuff kind of ready by then for that, like, that… that would all line up really well.
Michele Mancioppi 00:38:09 It would be pretty compelling to make a workshop together with the operator.
SIG. I mean, there is Jacob that is, working on using the injector inside the, the OpenTelent Operator.
And having a story where, hey, this is how you do it on Kubernetes, and this is how you do it on online access hosts, or inside a container image, that is, that is compelling, I find.
Ted Young 00:38:34 That's good. I… the operator's kind of next on my list to… to go join their SIG and talk to about… what does 1.0 look like for the operator? And, I know Jack Berg has… has… we did some spikes on doing this, but I… not clear to me, because I haven't talked to the SIG yet, how aware they are of this stuff.
Michele Mancioppi 00:38:56 I spoke with Jacob, so I was passing down the lessons learned in building not one, but two operators that do automatic instrumentation using injectors.
The, it seems to me the biggest hurdle is, redesigning the CRD.
The current CRD has a whole bunch of knobs and levers to twist, because somebody said that otherwise they would die without it.
Which makes, the experience effectively foot guns all the way down.
And very difficult to understand.
Ted Young 00:39:31 That's my… my biggest concern with the operators, just they've already designed a configuration language, right? And a set… they've made a set of decisions, right? And… and we're now coming to them and saying, like, we want to… We want to make breaking changes to that to have them conform to, like.
The way we want to do it.
Michele Mancioppi 00:39:50 That is, with CRDs and CRD versioning.
that is fine, to do in a backwards-compatible manner. I mean, you end up maintaining 3 different ways of doing the same thing, and… Unfortunately, in the age of LLMs, only the stuff that is used the most is actually visible to the LLM, but… Theoretically, we could do something better there.
Ted Young 00:40:11 Yeah, I think it's fine. I think that SIG also… I want to check the staffing of that SIG, because I think they might be understaffed a little bit to… but at any rate, I'm very hopeful that we can be in alignment, and yeah, if we're showing up with System packaging, if, like, we have declarative config mostly available in the languages that people use, right? And then we have, system packaging for those languages, and the Kubernetes operator, and they all have kind of the same configuration story. That's, like, a very compelling thing to sort of reboot.
you know, our marketing around OpenTelemetry, if you want to use those terms.
And our, and, like, our, like, like, just reboot our community engagement.
with a totally new narrative about how you do hotel.
That's more focused on, Kind of managing it like an operator at scale, and… The final piece of that is also OpAmp.
And making sure OpAMP also supports the kinds of things we're talking about.
Michele Mancioppi 00:41:20 That was bizarre.
OPEMP is interesting.
So, the, the way I understand it, It is… compatible?
in large extent, with declarative configuration, where, like, for example, we could make, like, if you want to use OpAMP, then congratulations, your declarative configuration says, use OpAMP, and then the SDK comes up, reads that, turns on OpAMP, and it gets whatever. So that thing, I don't see… big issues. I was surprised to learn that actually we're building op-amp in some of the SDKs, like Java. I thought it was only a collector thing.
That was wrong.
Ted Young 00:42:00 It's for the SDKs, I don't know if anyone's doing it outside of Java, yet, you know what I mean? Like…
Michele Mancioppi 00:42:07 It's an aspirational doing that for Node and Python?
Ted Young 00:42:11 Great.
Michele Mancioppi 00:42:11 But the challenge, I suppose, is going to be that it requires re-instrumentation.
And I… there are many languages where that is not possible.
Ted Young 00:42:22 Re-instrumentation, you mean dynamic? Right, well, you can…
Michele Mancioppi 00:42:29 Reinstelementation, imagine the case that… And again, this is what I know from other technology, maybe note of somehow it's different.
But, imagine the case that, I was explaining to you how Node.js instruments, right?
Until the instrumentations are up, your production code cannot run, because otherwise, if it does a require that it's not intercepted by the SDK, that code doesn't get instrumented, yeah?
Which means that in a world in which you want to do OPAMP, and OPAMP gets to give you configurations about which instrumentations you want to run and which not.
Before the application code actually starts.
you need to get OPAMP configurations, and if OPAMP tells you that, yeah, you know, you should turn this instrumentation on.
You cannot do that. The thing is that. Unless you rewrite instrumentation that is always instrumented, but somehow inert.
Huh?
It's difficult.
Ted Young 00:43:28 Yeah, I think what can… what kind of configuration changes can be supported? I mean, this is just an area we have to look at. The primary thing people want to control with op-amp is… is more, like, remote sampling, and… things like that, right? Like, there's plenty of uses for op-amp that aren't related to controlling your instrumentation and auto instrumentation.
Michele Mancioppi 00:43:52 It's the part why I like the clarity configurations, because Which instrumentation we want in the system packages, because we will need to install all of them.
Ted Young 00:44:02 Yeah.
Michele Mancioppi 00:44:02 So you need to disable the ones you don't want.
Ted Young 00:44:05 Right, it's just about having this… the same plan of, like, some people want to control all of this through Kubernetes, some people want to control it through system packaging. A lot of people are going to be working with a vendor, right, that's managing all of their observability stuff.
You know, like, that's… that's the third common pattern. And it's just… Yeah, making sure that that all actually works.
Michele Mancioppi 00:44:33 Although, from experience, The vendors are also cooking with water.
So the same mechanisms that we would use in system packages to decide which… what to turn on and off, the same would do… we actually have it in the concept. I mean, the idea of a vendor being able to provide a language-specific package it's one of the reasons why there are those virtual dependencies, so the test Java instrumentation thing can satisfy the Java auto instrumentation, and then if you install the test one, you don't install the community one.
Ted Young 00:45:06 Literally nothing we're doing is new, right? Like, these are all standard things. It's more just, like, no one has gone to the SIGs and been like, this is the plan.
to… to do this with OpAmp in all the languages in some way, shape, or form, right? It's more like… like, we have… this is not something we've written down as a plan and socialized with the maintainers as, like.
how to do it or what to do it, and so that's really my only concern about OpAmp, is like… like, we need to, like, have a plan for, like, how that should work, and make sure maintainers are onboarding with that. It's almost like… a little bit scary that SIGs might be going out and implementing something with OpAmp, and maybe they're all doing something weird with it.
But… That's… that's on my checklist as part of, like, this GA push, is just to make sure.
like, the roadmap for OpAMP makes sense, and, the maintainers are kind of… Aware of what that means for them.
Michele Mancioppi 00:46:13 By the way, is there a consolidated, reliable overview of which languages support the declarative, configuration?
Ted Young 00:46:24 There is not yet. You know, we have a thing on our website that's very limited around, you know.
do you support tracing metrics logs? And then we had this, like, unbelievably complex Matrix of, like, feature support.
So let me see… And that was in the spec.
And we were looking at just deprecating that thing, because it… It had gotten to the point where it wasn't… it was just too many things and wasn't particularly useful. Let me see if it's still there.
Michele Mancioppi 00:47:02 For example, I know that Java has the leading implementation for declutter config. I know that Python doesn't have any of it.
Night, I'm confused about it.
Ted Young 00:47:12 Yeah.
Here.
Here we go.
The question is always, you know, How up-to-date this is.
I'll put it in the meeting notes.
I can find…
Michele Mancioppi 00:47:26 Can you maybe also, share the screen?
Huh.
And I think I was wrong about Python.
Huh.
Ted Young 00:47:44 But if I just…
Michele Mancioppi 00:47:45 Interesting.
Ted Young 00:47:51 Here.
So, in the spec repo, there's this spec compliance matrix.
Michele Mancioppi 00:47:57 Yeah?
Ted Young 00:47:58 And… Where, you know, we've tried our best to keep track of what in the spec has been implemented where.
And… So this is kind of useful for maintainers to keep track of their own shit, but it's not very useful for, like, an end user at this point to come in and be like, what's supported where, right? Because, look at this.
You know, it's, like, endless at this point. There's so many features.
But declarative config is in here.
To a certain degree.
Michele Mancioppi 00:48:36 I think it might be outdated, because, for example, for Python, I am seeing… this.
And that looks suspiciously like an implementation of the declarative config format is just a partial one.
Ted Young 00:48:59 Right. So, they may just be underway and haven't updated this yet.
With this.
Michele Mancioppi 00:49:07 Should we go and figure out… Which ones are actually implemented right now?
Ted Young 00:49:14 Yeah.
But, yeah, it's the kind of thing where, you know, all the SIGs are kind of working their way through this at their own speed, but, In terms of, like, letting the end users understand what's available where. Like, we don't have… We don't… the only thing we have there is, you know, this.
So we have this status page.
Right.
Which itself may be a bit out of date.
But something like this could possibly be… Improved or extended to include some of these other high-level things, like declarative config or packaging or something like that.
Michele Mancioppi 00:50:07 Yep.
Let me share the screen again.
Make sense?
Alright.
So, if we want to… make a splash at KubeCon.
That means that, I mean, we need to go to The famous cubicon-driven development, and we need to work backwards, right?
it works. I'm not… I'm not gonna, gonna, sin… I'm not gonna talk about… it's a system that works.
Ted Young 00:52:11 You're talking to people who work for Grafana, we basically do nothing but conference-driven development over here, so we're fine with this.
Michele Mancioppi 00:52:18 I'm sure your marketing people love to have this on the public record.
The.
Ted Young 00:52:26 It's great to know when you're gonna announce things, and, like, but yeah, KubeCon in A, I think, is the perfect target. I think it's just far enough away that… that we can really get… get something useful out the door in at least a couple of languages.
Michele Mancioppi 00:52:41 the, I would love to have a couple of months of user feedback.
Which users… I don't know.
Ted Young 00:52:55 Yeah.
Michele Mancioppi 00:52:57 The… which means that we would have to have something working End of July.
And then we're working backwards from there, I mean, setting up the creation of the packages, I mean, the building steps.
It's not difficult, the hosting is difficult.
So, the… The first thing we need to solve is the hosting bit. That's the highest priority, and that is the critical path.
The most critical of paths.
Ted Young 00:53:27 Right.
Michele Mancioppi 00:53:27 The rest follows.
Ted Young 00:53:30 Well, it seems like we already have prior art, right? So, we can… Kubernetes has already, like, picked a path for distributing this, but then we also have… and then the collector has already picked a path for key signing and things like that, so hopefully we can just glue those two things together.
In some way, rather than try to do something new.
Michele Mancioppi 00:53:58 Yeah, I would love not to have to reinvent.
APT and RPM back.
Package hosting that will be announced.
Ted Young 00:54:07 Yeah, also, OpenTelemetry doesn't have a bank account, so things that cost money don't.
Michele Mancioppi 00:54:12 Yeah, there's a little bit of food to cloud bill, that's not an issue.
Okay.
Then, Denise, you take the… you look further into the hosted packaging, and I start, the thing about the creative SDK and versioning?
Denys Sedchenko 00:54:32 Yay.
Michele Mancioppi 00:54:34 So I will focus on the… as we already said, the versioning is not for the first release, so I'll focus on the… the, decorative configuration.
This bit I'm actually gonna put back in the box, because I'm not gonna do it in the near term.
Ted Young 00:54:54 Yeah, there's versioning schemes, there's just also the basics of being able to turn things on and off, right?
Michele Mancioppi 00:54:59 Yeah, that is the creative config.
Ted Young 00:55:01 Right, yeah.
Michele Mancioppi 00:55:03 This is, I mean, this is near and dear, because the… not all instrumentations, by far.
Are of equal quality.
by far, not all instrumentations are desired by users. For example, there is a whole bunch of stuff about opening TCP sockets in Node that I have no idea why it's there.
So that is, that is pretty important.
Ted Young 00:55:28 I think there's… there's another track around, you know, OpenTelemetry GA that's about… you know, wrangling instrumentation, right? And I think that's… that's gonna be a big part of that, right? Like, instrumentation has just been the Wild West in open telemetry, and we want to develop some better tools and make it more compelling for organizations to take on the responsibility of maintaining instrumentation, but a side effect of that is also, like.
you know, we don't want to take on everything in Contrib, and maybe there are some things in Contrib that should just be deleted, or, you know, deprecated, or…
Michele Mancioppi 00:56:11 My opinion on this thing I agree with you on 50% of what you said in the last two sentences. So, some staffing contribute should be deleted. Yes.
We do not want to maintain all of contrib.
Let me give you the stink eye, because that is, like, canonical saying that we have universe, but, you know, it doesn't work.
That is, like.
Ted Young 00:56:35 Well, that…
Michele Mancioppi 00:56:35 That's what I'm.
Ted Young 00:56:36 You know, like, there's, like, we… sometimes people are like, oh, the most popular stuff, let's only support that. And I'm like, that doesn't work, because everyone's deployment is, like, is this long tail of things, exactly. You can't just use popularity to judge What… what is important.
What I'm saying, though, is there may be some things in there that are just, like… genuinely, like, crap, right? You know, like, we can't say that anytime someone shows up out of the blue and wants to, like.
Donate a couch that we're gonna put it in our house.
So… and to some degree, we've been maybe reflexive about being like, sure, we'll take all of these things. So that's all I mean, is like… like, I do think it's on us to maintain the ecosystem of the instrumentation that we need, and we need to come up with better incentives for… For making that attractive.
Michele Mancioppi 00:57:37 For example, the moment we have turning on and off in the declarative config, in the languages that we care about for system packages, the first level of curation Is the faster to ship by default.
So there… sure, you can put DNS instrumentation in Node. I ain't turning it on by default. That's just zero sense.
Ted Young 00:57:57 Yeah.
Yeah, so, you know, do we ship, like, a giant default configuration? Like, how do we… how do we do that for people?
Michele Mancioppi 00:58:07 I mean, it's always easy to start, like, going there and just go, yes, yes, yes, no. The moment that you start small and then you add more, adding more is always easy. Taking it away is what breaks people, right?
Ted Young 00:58:21 Yep.
Thank you.
Michele Mancioppi 00:58:23 They can also break people by adding more stuff, but…
Ted Young 00:58:25 Yeah.
Michele Mancioppi 00:58:26 It's less common.
Ted Young 00:58:26 The main thing is, right now, it's all completely theoretical, because we don't have the… we don't have the humans We do not have humans signing up in droves to, like, take on the maintainership of this stuff. The stuff that's out there is somewhat maintained. Like, the first step in this, honestly, is, like, an audit. Like, which of these contrib repos actually have active maintainers?
Right? They might be community members, who knows who they are, but, like, which of them have somebody who responds to pull requests and is keeping them updated, and which one…
Michele Mancioppi 00:59:03 I looked up, I looked up…
Ted Young 00:59:04 donated, and that person has moved on. Like, on paper, most of these things have maintainers, but a lot of that is probably BS, right?
Michele Mancioppi 00:59:14 I looked at the amount of open PRs and open issues across the SDKs and contributes.
You will be surprised how many have more than 50 per type.
And a few are in the three digits.
Ted Young 00:59:30 Yeah, no, I mean, it's super bad. Like, the two things that I see are bad is, like, a number of these repos don't have containers, right? Or… or a nominal maintainer, like, maybe this month they look at things, maybe next month they don't.
And then the other thing is just, it's… it's hard to, like, push changes out right now. Even when things get updated and contrib, if you wanted to rush a security patch or something like that, right? Like, that whole process is, like, very slow, and so just wrangling all of that.
and my hope is, like.
some cool stuff with Weaver and whatnot to… if we could make it more interesting.
to maintain this instrumentation, I think that might help.
Michele Mancioppi 01:00:24 As somebody who has created multiple infrastructure code tools recently only by clodding it, and has written instrumentation in the past.
I applaud your optimism.
Instrumentation is orders of magnitude harder.
And I'm not sure… at the current state of the art, how well AI can cope with that.
There is an art to that that doesn't exist in other types of softwares.
Ted Young 01:00:48 Yeah, I mean, have you… have you checked out Weaver at all?
Michele Mancioppi 01:00:54 Yeah, yeah, we're using it internally. We published our own semantic conventions, yes?
Ted Young 01:00:59 Cool. So, like, to some degree, the hope is, like, if we can generate enough primitives and enough of a test harness, how much can we box the AI in? But like you're saying…
Michele Mancioppi 01:01:11 But I don't believe that's the case, because the hard part is not which semantic conventions I apply. It's how the hell do I do it with yet another HTTP client? Because all the internals are different. Oh.
Ted Young 01:01:22 Yeah, I, I, I seriously, I have no hope for, like, AI… taking AI and pointing it at some new library and be like, go do this for me. I think it's much more about, like, how do we take this giant pile of stuff we already have and, like, re… change the way that we're managing it? Because if the way that we're managing it is every single library has, like, some random person on the hook is the maintainer for that instrumentation library. That's the thing that feels like it doesn't work right now. And, like, is there a way to take… to just change our ownership model for instrumentation. And my hope is that these AI tools would at least help Be able to, like, generate… you know, like, update PR. Like, we have a whole bunch of stuff that's, like, it's at some random state in terms of… which semantic convention it supports. And at least being able to, like, take all of those things and be like.
like, getting it up to date. But anyways, it's a big lift, and we don't have the people, so figuring out how we're going… I don't know if it's just a consortium of vendors.
you know, we're at time, and we're off-topic, but, like, some way of, like, wrangling. The whole point is, like, we wanted to share the cost of maintaining all of this stuff.
But the end result, predictably, is a tragedy of the commons. So, how do we get out of the tragedy of the commons? Like, what… what… What incentives can we provide for people to maintain this stuff, even though it's not sexy, it's boring, right? Like, what… what kind of rewards or anything can we offer, to… To make sure this stuff is, like, kept up to date.
Don't have great answers to that yet. That's, like, the one… of everything on GA, everything else is straightforward. It's the one piece of the puzzle that it's, like, a human social problem, not a… not a coding problem.
Michele Mancioppi 01:03:30 Well, I'll repeat it again. If there are maintainers that, for example, had to… like, it happens that companies' priorities change, and all of a sudden, instead of working on auto, you're doing something else entirely.
Ted Young 01:03:44 Yeah.
Michele Mancioppi 01:03:45 I have positions, and they're zero to staff maintainers. I already started hiring a few.
They're gonna come, I'm in the process of hiring a few. I am looking for, ideally people that were maintainers before, and they cannot any longer because work moved them somewhere else, then you want to do it almost full-time, come and talk to me.
And I… or people that have been active in the community, but their work is not about open telemetry, but they would like to do it full-time.
I am less interested in poaching active contributors from another vendor, because that's a zero-sum game.
I prefer to bring more people into OTEL than just having more maintainers under the FE filter, because that is pointless.
Ted Young 01:04:29 And that makes sense for, like, SDK maintainers and the like, and we want to work as a community to figure out, maybe something more like a fast track for getting people to approve your status, right? Because that's… that's the other thing, is like… companies want to staff these SIGs and bring people in, but then it's just like… You know, like, what…
Michele Mancioppi 01:04:53 is the cushion.
Ted Young 01:04:54 of, like, how quickly do you give them a hat and say, you're responsible now, go do it, versus, like.
Michele Mancioppi 01:05:00 Is it really the bottom like that?
Ted Young 01:05:03 Sorry, what?
Michele Mancioppi 01:05:04 Is it really the bottleneck?
Ted Young 01:05:06 Is it the bottleneck? What do you mean?
Michele Mancioppi 01:05:08 Because I have never seen a company wanting to stop somebody to do maintainership, and they did a good job, and they didn't get a maintainership.
Ted Young 01:05:17 No.
Michele Mancioppi 01:05:17 It's good.
Ted Young 01:05:18 I, I think it's more the… about, Going to com… if you're going to companies and you're making an ask for them to commit more resources.
it's, like, how do you have that conversation? And for SDK maintainers, it's not as bad, but if we're gonna say, like, we need to really ramp up to also include, like, instrumentation as part of that.
that involves going back to, like, all of the existing companies that currently contribute to OTEL and be like, how are we gonna staff this?
And, like, there just needs to be some kind of, like, plan as part of that proposal, other than, like.
banging on a pot and be like, everyone's… go help us with, like, that… I just don't see any hope of, like.
That, because, like, the instrumentation is so… boring and uninteresting, you know what I mean? Like, it's the kind of thing everyone.
Michele Mancioppi 01:06:12 I understand what you're saying, I do not understand the semantic, because instrumentation is wonderful, but… I understand the semantics that you apply to it, not how it applies to me.
Ted Young 01:06:22 Yeah, yeah, I just don't know how we get, get people to contribute effort into this area without offering I don't know, like, I don't know how to package that up yet. Anyways, we're over time. We won't solve it today.
Michele Mancioppi 01:06:37 Then, people, it was a pleasure, and see you next week.
Ted Young 01:06:41 Right?
Denys Sedchenko 01:06:42 Bye.
