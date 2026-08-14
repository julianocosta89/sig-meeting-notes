SIG: Packaging SIG
Date: 2026-08-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado** 02:22 Yeah, Antoine?
**Antoine Toulme (Splunk Inc.)** 02:24 Goodingo.
**Diego Hurtado** 02:27 Let's just… I hear about myself, on the ring.
Where's everybody.
**Antoine Toulme (Splunk Inc.)** 02:33 Okay.
Let me open the notes.
**Diego Hurtado** 02:41 Are you in a different place? Where's your Pac-Man machine? It's a Pac-Man machine, right?
**Antoine Toulme (Splunk Inc.)** 02:47 If you don't see the.
**Diego Hurtado** 02:47 It's right there.
**Antoine Toulme (Splunk Inc.)** 02:48 Okay.
**Diego Hurtado** 02:49 I cannot see it, I can't see a very… That close-up of your, of your face.
**Antoine Toulme (Splunk Inc.)** 02:56 It's doing the wrong… Oh, what happened?
**Diego Hurtado** 03:00 How many cameras do you have there?
**Antoine Toulme (Splunk Inc.)** 03:02 It's just estimate.
It's my camera for my… for my laptop. Oh, okay, USB-C.
**Diego Hurtado** 03:09 The camera's moving.
**Antoine Toulme (Splunk Inc.)** 03:11 Yeah, yeah, on Macs now, they have… they follow… Like, your mic's supposed to help you kind of recenter on your face.
Which… Oh my god.
Not that useful.
**Diego Hurtado** 03:24 Does it make you feel like, like, reporters are following you with their cameras and your famous paparazzi and stuff?
How do you deal with all that, Antoine?
**Antoine Toulme (Splunk Inc.)** 03:35 It doesn't make me feel very special, I gotta say. Thank you.
**Diego Hurtado** 03:38 But you're special.
**Antoine Toulme (Splunk Inc.)** 03:40 I think I abandoned that hope a long time ago. I thought I was special for a while, and then I met people, and I'm like, oh… There are people who are much better at what they do than I am.
**Diego Hurtado** 03:51 But, I'm pretty sure I talk for everybody in this call when I say that you're special.
**Antoine Toulme (Splunk Inc.)** 03:58 Cool.
**Diego Hurtado** 04:01 It reversed me.
**Denys Sedchenko** 04:02 Hello, guys.
**Diego Hurtado** 04:03 We appreciate you very much.
**Antoine Toulme (Splunk Inc.)** 04:06 Thank you, Jigo. Hey.
I think, I think Jiggles Little Talk made everybody come over, which is cool.
And that is completely open right now, so… Put your stuff in there, please. What do you want to talk about?
**Diego Hurtado** 04:23 Well, some killer here… Hilarious.
**Antoine Toulme (Splunk Inc.)** 04:28 Yeah, probably some…
**Diego Hurtado** 04:29 I'm Michele.
**Antoine Toulme (Splunk Inc.)** 04:30 Michele you… It's good to see, Jacob here. How are you?
**Jacob** 04:38 Have you guys been moving from this call to the injector one? Or… because they're different Zoom links.
**Antoine Toulme (Splunk Inc.)** 04:44 We're doing, We're doing Packaging at 8, or 11 your time, and then, injector at, 8.30.
**Jacob** 04:52 Yeah, I saw that, but are you, like, switching calls, or are you staying on the same call?
**Antoine Toulme (Splunk Inc.)** 04:56 We, we switched cars.
**Jacob** 04:57 We switch goals, okay.
**Antoine Toulme (Splunk Inc.)** 04:58 We try to be good about this, yeah, because this recording is gonna have to be about each SIG, right?
**Jacob** 05:04 Yeah, yeah.
Are we still posting those? I don't think we are.
**Antoine Toulme (Splunk Inc.)** 05:09 Well, it's a new thing now. Actually, Ted, you might know that.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:12 Yeah, the whole thing has been switched to, The Lynx Foundation's been creating a platform called LFX to kind of run everything out of, and they have a whole Zoom platform now. So you'll notice the links now, when you go to them, it asks you to sign in to this LFX platform.
And if you go to that platform for every past meeting, you can see the Zoom recording. So it actually works, a lot better than our janky setup before, where we had to juggle, like, 4 or 5 Zoom accounts, and… And play a map coloration game where we did not put, like, more than two, two meetings with the same account back-to-back.
**Antoine Toulme (Splunk Inc.)** 05:59 Yeah.
**Jacob** 06:00 Good bin packing problem, but I'm glad that it's fixed.
**Ted Young (Raintank, Inc. – Grafana Labs)** 06:03 Yep.
**Antoine Toulme (Splunk Inc.)** 06:08 Alright, we got one item.
**Michele Mancioppi (Dash0 Inc.)** 06:11 It's a very cool item. I mean, Denise is doing really cool stuff.
**Denys Sedchenko** 06:17 So, I will start.
So, at last call, we talked about Fedora Copper.
I have a POC, and I have a PR for it.
For you to review.
And, if we're good to go, we would need to create an organization, an account on Copper.
and also a project, so I can, like, update the workflow, so it will use not my personal, but actually, like, the OpenTelemetry official account.
Besides that, I… created, blob storage.
on Cloudflare.
Plus, I had a custom domain, and, like, added in a separate branch, not in a branch where my PR is open, it's like a branch of a branch.
to actually… to actually mirror cop… what we have on Copper, to mirror to that blob storage, last attach the custom domain.
And also, in Hartel Packaging chat, I gave instructions how you can, like, try, how you can try to… use the mirror domain as a repo, so we can, like, Go and try To check if it's actually working. I tried it locally in my Fedora VM, for me it's worked.
But basically, like.
All the technical requirements, I assume are satisfied for Fedora, and we can do… similar way.
for, Launchpad.
**Michele Mancioppi (Dash0 Inc.)** 08:04 And your POC also has the index that contains Multiple versions of a package, right?
For the payment.
**Denys Sedchenko** 08:12 So currently, I basically mirror everything that I have in Copper, and my Copper repo contains multiple builds. So basically, every time I trigger a new build, it creates a new version, and Copper basically contains all the builds I previously triggered. Those are, like, the versions.
**Michele Mancioppi (Dash0 Inc.)** 08:33 I think we should pull the trigger and just do it.
**Antoine Toulme (Splunk Inc.)** 08:37 Do we want to… involve, the DC to own the Copper account and Cloudflare account?
**Michele Mancioppi (Dash0 Inc.)** 08:46 Find the domain, yeah, sort out the domain, yeah.
**Antoine Toulme (Splunk Inc.)** 08:52 The main seems, like, quaint, because it got that, but…
**Michele Mancioppi (Dash0 Inc.)** 08:57 You still need to go and configure DNS records and pointy touch stuff.
**Denys Sedchenko** 09:02 Yeah, true. In my case, it was very, very simple, because my domain was managed by Cloudflare, so, like, for me, it was just one click, but I don't know where your… where the OpenTelemetry domain is.
And also, what you actually want to use as a blob storage.
Cloudflare has open source program support.
But maybe, but maybe we already have an actual blob storage to use.
**Michele Mancioppi (Dash0 Inc.)** 09:29 As far as I know, And that is secondhand information. The OpenTech website runs on Netlify.
Which is not exactly the platform you would use for blob storage.
So, it will need, depending how the domain is managed, if Netify is managing it, then that needs to be moved out, so that you can add another record for packages.opentelemphry.io.
And then, bit, points, we need a, But by the way, you tried it on Cloudflare. That, did you put it directly under the root of the repository, or did you put a path in front of it?
**Denys Sedchenko** 10:10 So… Basically, I put it under the path, so basically, I have a subdomain, otel.pkg.
**Michele Mancioppi (Dash0 Inc.)** 10:18 Excellent.
**Denys Sedchenko** 10:19 exponunix.dev, and there, basically, I have a RPM subdirectory.
**Michele Mancioppi (Dash0 Inc.)** 10:24 Okay.
**Denys Sedchenko** 10:24 where it's happening, because I've done this in assumption that we could use the same domain for the Debian package.
**Michele Mancioppi (Dash0 Inc.)** 10:31 Exactly. That's exactly what I meant. So, effectively, what we would do, we would put in the same storage bucket RPM and DVM packages.
And then, put a… More documents there at the root, in case you get there and you don't know what, what you see.
Which is effectively what we did in the POC with GitHub pages.
**Denys Sedchenko** 10:53 So, in my case, it's just to hold the main points to block it.
But Packet has subdirectories for different, like, package… like, different…
**Antoine Toulme (Splunk Inc.)** 11:03 Damn.
**Denys Sedchenko** 11:04 Distros, like Carpi and Debian, etc.
**Michele Mancioppi (Dash0 Inc.)** 11:08 Could you… I am, I am swamped. I've been trying… I've been meaning to review your PR, and I even made an analysis of what you need to backport.
Could you please take the stuff of CNI and try to do the same, with the same Cloudflare bucket?
Because if that works.
I think we have packaging as soon as the GC can, can actually go and give us the… The accounts, yeah?
**Denys Sedchenko** 11:39 Yeah, but I would like to do that separately, because, like, I already have a lot of stuff just for the Fedora.
**Michele Mancioppi (Dash0 Inc.)** 11:49 Sure.
**Denys Sedchenko** 11:50 Thanks, but yeah, it will be definitely possible to do the same from the launchpad.
**Michele Mancioppi (Dash0 Inc.)** 11:56 I mean, effectively, the criterias that we set out in the very beginning, the only thing that this will not accomplish is the signing key.
Which… Given the fact that we did not find a way to get everything.
Is the least annoying of the options.
**Denys Sedchenko** 12:16 Regarding signing, right now, Fedor Copper manages the signing.
And I even, like, in the instructions, I have the RPM import command, which imports the signing key.
that public, that public key, I actually, like, it's mirrored from the copper repo.
Like, I don't, like, own it, I just basically mirror everything in blob storage.
**Michele Mancioppi (Dash0 Inc.)** 12:43 Yes, but the thing is, at the moment we need to move off copper, then the private key changes, so the public key changes too. It's not about the mirroring, it's about the private key used for signing.
But I think that it's a supplement.
I think that this is… this is acceptable. I mean, because if you want to have full control, then we need to effectively make our own… our own thing, which would be terrible, and this gets us so close.
to a really good solution that is, it's a really good solution, the only thing is that there is the risk that the signing keys for RPM and or a TBM change over time.
Okay.
**Denys Sedchenko** 13:20 I assumed it's… risk that will be, like, even if we own the key, we still will have this risk, because let's assume, hypothetical situation, that, signing key leaks.
And if it leaks, we'd need to rotate the key. And rotating the key leads to the same outcome.
**Michele Mancioppi (Dash0 Inc.)** 13:37 Yes.
True.
**Denys Sedchenko** 13:41 Thanks.
And guys, if anyone has time, please check the Hotel Packaging channel, check my message, and try to play.
as well.
**Antoine Toulme (Splunk Inc.)** 13:50 Will do.
**Denys Sedchenko** 13:51 Thank you.
**Antoine Toulme (Splunk Inc.)** 13:53 So now we're… we have some admin to do. So that… we do… Would you please help me here, on all those requests? Because we have a fair amount of, request towards getting infrastructure. We need a copper account.
Yeah.
**Denys Sedchenko** 14:10 I need to…
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:10 Piling it into a community issue, that's the easiest way.
**Antoine Toulme (Splunk Inc.)** 14:15 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:15 As long as there's one place where we're putting all the things we need to pay money for,
**Antoine Toulme (Splunk Inc.)** 14:23 I don't know that I'll have to pay my… actually, that's the thing, it's like, you're going to exchange time for money.
Because you have to talk to them a little bit more to get, like, part of their free program.
Which I'm sure they would actually be… Probably targeting us for, but…
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:38 Yeah.
**Antoine Toulme (Splunk Inc.)** 14:39 That might cause us to spend time on that.
Okay, so, open a committee issue… For all… Accounts requested.
Denys, you're about to… to be more precise, so copper, Cloudflare… the domain.
**Denys Sedchenko** 14:57 Yeah.
**Antoine Toulme (Splunk Inc.)** 14:57 else.
**Denys Sedchenko** 14:58 Yeah, and I had a couple of secrets.
when, basically, when my GitHub workflow uses a couple of secrets.
So, it uses the Copper config, which is… contains, basically, API token and everything that Copper CLI needs to work on the GitHub workflow, and besides that, it's… And to upload stuff to S3… upload stuff to blob storage.
I have a… I have a token that I created on the Cloudflare site. Basically, it's, S3 credentials. You have access key, ID, secret key, and, like, the… And, the S3 endpoint.
**Antoine Toulme (Splunk Inc.)** 15:43 I see.
**Denys Sedchenko** 15:44 Dm me if you need any extra information. I can, like, show you what they have, like, on the… secret site on GitHub.
**Antoine Toulme (Splunk Inc.)** 15:53 Okay, so for those… we don't have a way to put secrets right now in our package repository, right?
**Denys Sedchenko** 16:00 It's… right now, I'm using just plain GitHub Secrets.
**Antoine Toulme (Splunk Inc.)** 16:03 Denim, yeah.
**Michele Mancioppi (Dash0 Inc.)** 16:05 Yeah, that's actually… I find it confusing that I'm not an admin of the GitHub repo.
**Antoine Toulme (Splunk Inc.)** 16:11 I mean, he'.
**Michele Mancioppi (Dash0 Inc.)** 16:12 Perfect.
**Antoine Toulme (Splunk Inc.)** 16:13 It's all done through this separate project that's using Terraform to manage the overall organization.
And that means that we don't use GitHub Secrets in that capacity, so… I think we've been using a shared vault, in some cases, to store stuff.
For the collector… I don't know… Shared one password vault, sorry.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:39 Yeah, we use 1Password for human secrets.
**Denys Sedchenko** 16:43 Great.
It's a… also, it will… it will resolve potential possible security problems.
But if there is a way for the job to ask those secrets from vote.
Or, like, 1Password is not a problem for me.
I just need to obtain them from somewhere.
**Antoine Toulme (Splunk Inc.)** 17:05 Yeah, exactly. So… This has probably come up before, come on, right?
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:14 It's worth figuring this out, you know, relative to how we manage secrets for the collector, for GitHub admin access, all of these things, but just a community repo issue for all of this, so we can kind of get it standardized, because that will be… it will be helpful for… this stuff to not get lost, right, or only be held in the heads of the current maintainers of the packaging SIG.
**Antoine Toulme (Splunk Inc.)** 17:40 Oh, yeah.
I don't wanna… I don't wanna be responsible for… Holding that, 1Password Vault… find a… Best practice approach to manage.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:53 Yeah.
**Antoine Toulme (Splunk Inc.)** 17:53 Prince.
We need them in GitHub.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:57 Yeah, and maybe this is actually, like, two issues. One is getting access to the physical infrastructure, right? Another one is, like, hey, we're collecting a bunch of different secrets, how are we supposed to manage these?
**Antoine Toulme (Splunk Inc.)** 18:12 Okay, Michele and Denise, I think you mentioned you were going to be out for a couple weeks. Is that in the coming weeks? Is it next week?
**Michele Mancioppi (Dash0 Inc.)** 18:21 No, it's end of, so last week of August, so I have another couple of weeks, which means that if we get the infrastructure, I'm more than happy to do, to do the work, to onboard stuff as much as I can.
**Antoine Toulme (Splunk Inc.)** 18:33 Understood, that's… that was my next question, thank you.
**Michele Mancioppi (Dash0 Inc.)** 18:36 That was an obvious next question.
**Antoine Toulme (Splunk Inc.)** 18:40 Well, I mean… Whatever we can do.
**Denys Sedchenko** 18:45 Me and Ted also will be out.
From the last week of… from the 28th of August till the 5th of September.
**Antoine Toulme (Splunk Inc.)** 18:54 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:56 I'll be out the week before as well, but I'm not… I'm not of particular value at the moment, so that's fine.
**Michele Mancioppi (Dash0 Inc.)** 19:02 Ideally, we do it either before, Or after.
I,
**Antoine Toulme (Splunk Inc.)** 19:08 I don't think we're gonna have a good time just asking all those requests of the committee, it's just a lot of minutiae.
So… I wouldn't hold my breath that we're gonna get done in a week.
That's what it is.
So, you can go on vacation, and we… you can be fresh when we get back in, you know.
Turn that on.
I wanted to just make sure we… Anyway, I'll let you know. I'm gonna open that community issue today.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:43 I will poke people to make sure we at least get answers to all of these questions quickly.
**Antoine Toulme (Splunk Inc.)** 19:50 Yeah, I feel bad, I've been asking Trask thousands of questions.
Yeah, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:56 That's kind of why I wanted to be a community issue, because a lot of this gets funneled to DMs to Trask, and he's, like, super busy, but I feel like Severin and other people also…
**Antoine Toulme (Splunk Inc.)** 20:05 No. No idea.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:07 Excellent.
**Antoine Toulme (Splunk Inc.)** 20:08 Yeah, you're right. Okay, Well, good job, Denny, anything else today?
**Denys Sedchenko** 20:19 Nothing on my side.
**Antoine Toulme (Splunk Inc.)** 20:24 Hmm…
**Michele Mancioppi (Dash0 Inc.)** 20:26 There is, an interesting discussion going on in our channel with, one of the maintainers of Python about do's and don'ts.
So the situation with Elasticsearch instrumentation.
**Antoine Toulme (Splunk Inc.)** 20:39 I see, okay?
**Diego Hurtado** 20:45 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 20:46 I think there is some education to be done, but it's, I mean, we've already discussed it also in the material.
Somebody needs to own the specification in, about, when to re… when you get to drop support for something. Right now, it's so bloody random.
Dropping supports for, runtime versions, dropping supports for libraries, for instrumentations, it's like… It's random.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:13 So we… we have some very, very outdated docs in… in the spec repo that could get updated around support and lifecycle. Have a look.
**Antoine Toulme (Splunk Inc.)** 21:31 Okay, I'm gonna just link Nat in that… dope notes… Because… Discussion… Okay.
Alright.
**Diego Hurtado** 21:58 to admit it.
Okay, regarding that topic, Little good news.
Because, I think… This whole topic, about, stopping the release of any kind of, OpenTelemetry component.
This time, it was a summitations, but… the little good news is that I think, We may have a solution for this particular situation in Python right now.
I have a proposal that I want to discuss, in one hour or so with, the folks in the Python SIG. I'll update again in the conversation we have in the OpenTelemetry Packaging channel.
So I just wanted to… just to let you know that.
**Michele Mancioppi (Dash0 Inc.)** 23:10 Oh, in case you missed it, there was, in the maintainer call, there is, some time ago, there was the wish of getting updates from the SIGs, and, this week.
I gave an imprompt update of where we are with packaging.
Says there was nobody else prepared, so I said, yeah, why not?
**Antoine Toulme (Splunk Inc.)** 23:29 Okay. Take care, Michele. That's cool.
What was the reaction from, from folks? Was they happy with our progress, or… Of course, I think we're on track… Faster than the fart. Knee.
**Michele Mancioppi (Dash0 Inc.)** 23:43 I think Ted is better positioned to comment on that than I am.
**Antoine Toulme (Splunk Inc.)** 23:47 Would you…
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:48 What was that? I was trying to look up our maturity model.
**Antoine Toulme (Splunk Inc.)** 23:51 W, whoa.
**Michele Mancioppi (Dash0 Inc.)** 23:51 You were, you were in the maintainer call, right?
How do you think the reaction was?
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:00 I thought it was good. I mean, I think… I think it'll be helpful to demo this stuff more. I would love to get something onto our YouTube channel.
If you think we're ready for the public to start giving us feedback.
**Michele Mancioppi (Dash0 Inc.)** 24:17 I think the moment we do the publication of packages in the repo, we're happy with, yeah, it's full throttle.
**Antoine Toulme (Splunk Inc.)** 24:24 We're gonna get a ton of requests.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:28 Yes.
**Antoine Toulme (Splunk Inc.)** 24:31 Yeah, by the way, we should really, like, the community of OpenTeometry is really amazing. We, I added a receiver to the contrary distro, and two weeks later, I already got feedback, like, this, there's a lot of, serendity from folks using it. It's,
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:47 Yes.
**Antoine Toulme (Splunk Inc.)** 24:48 Yeah, it's a very big engine.
**Michele Mancioppi (Dash0 Inc.)** 24:51 I am waiting.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:53 Sorry, go ahead.
**Michele Mancioppi (Dash0 Inc.)** 24:54 I'm waiting still from the end users, from the ComSIG About, when, to go and talk about it in various podcasts and things they organized, it's… it seems lost in… In fog at the moment, unfortunately.
**Ted Young (Raintank, Inc. – Grafana Labs)** 25:11 Okay.
Point me at that, I'll try to help, get that unblocked. We, I feel like there's, like, a rule of open source, which is, like, The feedback always comes in.
the moment after the window for feedback is closed, right? Like, you're trying to get all the feedback during the release candidate, right? But it's, like, the 1.0 is the signal that causes people to give, and so it's always a question of, like, how do you trick people into believing you've released?
A 1.0 when you haven't yet?
**Antoine Toulme (Splunk Inc.)** 25:54 Yeah, we did a push on LinkedIn when we did the first GitHub pages, and There's a lot of… enthusiasm?
in… Yeah, but… I don't think we had too many issues. No, we actually had one issue that was interesting, worth discussing here, which is that currently in our GitHub pages, we only publish the latest version. We discussed that last week, really quickly.
And we… we're kind of, making the choice not to have the older versions. One of them is… one reason to do that is because it's GitHub pages anyway. We don't want to host, like, you know, terabytes of data. That's never been the point of this.
But the question remains, what is going to be our dependency management story? Do we want to keep, old releases around? How long do we keep them around?
What's the move there?
And…
**Michele Mancioppi (Dash0 Inc.)** 26:53 I agree.
**Antoine Toulme (Splunk Inc.)** 26:54 We can down the road on this one, for now.
**Michele Mancioppi (Dash0 Inc.)** 26:55 No, I mean, Denise gave us the solution for being able to keep older versions. I mean, putting in a stray in Cloudflare, fine.
And automatically, when you go and do a PTF grade or YAML upgrade, then it works.
**Antoine Toulme (Splunk Inc.)** 27:09 That's true. That works for me.
**Michele Mancioppi (Dash0 Inc.)** 27:10 And I'm… The, when we retire versions of packages.
**Antoine Toulme (Splunk Inc.)** 27:18 That's… that's what I'm.
**Michele Mancioppi (Dash0 Inc.)** 27:18 I believe it's more a question of how much money we want to pay for the buckets, because First of all, we… at the moment, we are lacking a policy of when to release new versions of a package, but in reality.
We should do it every time that a release train on an upstream SIG has released something. For example, the injector, I made a fix because we found a bug with old versions of Debian, released the injector, immediately released the package.
Java makes a new version of the Java agent, we should ship a new version of that package.
We have an issue about defining the versioning scheme.
But there we could do something as simple as taking the number of the release train upstream, Plus… an index, like, minus 1, in case we make a second release, because the shell scripts of the package have a bug, not the content, yeah?
**Antoine Toulme (Splunk Inc.)** 28:15 I think that's fine. All that is fine. I would say that… We will need to have some sort of a discussion at the OpenTementry level, then, where we would agree That there are diseases that are just too old to be distributed anymore.
Like, they can be archived somewhere, they could be available, but, you know, past 2 years, I don't want people to run a version of a collector.
I've seen this happen, right? So, people would, for example, run version 30 as a collector, because the version of Go that is compatible with it runs on Windows… is it 2008? 2012?
Something like that, like, that is no longer supported at all.
And, that's dangerous. Actually, we don't like to discourage this type of behaviors.
**Michele Mancioppi (Dash0 Inc.)** 29:01 But, I mean, realistically, right now, I don't think we ever deleted a GitHub release.
**Antoine Toulme (Splunk Inc.)** 29:07 Yeah, and this is where we should start, right? We should start by deprecating and archiving old releases in those repos.
First.
And have some sort of a sense And in that case, we would be downstream from that, exactly the same way that you want to make a new release when there's a new release upstream of a package that we depend on, it would also be archiving all the releases that are being archived upstream from us. Does that make sense?
**Michele Mancioppi (Dash0 Inc.)** 29:32 Oops.
**Antoine Toulme (Splunk Inc.)** 29:33 Alright, maybe we should just… I'll just document the offer, that would document that.
If we're okay with this approach… Let's do it.
**Denys Sedchenko** 29:43 I forgot to mention, just to be safe, my job also backs up what previously was on the bucket.
And a previous… as a previous, like, to a dedicated path, just in case we would still need some kind of, like, historical data in case, like, something… Like, some build gets lost on the copper side.
Yes.
**Antoine Toulme (Splunk Inc.)** 30:05 Okay, that's cool.
That definitely could be happening, like, systems tend to fail like that.
Yeah, we have to try your stuff. Okay.
Okay.
**Michele Mancioppi (Dash0 Inc.)** 30:34 A quick update about, support, for Ruby. It's, so the support of a language in the packages is contingent to a few things, like you can automatically inject it from a technical perspective, and second.
we can specify, the support metrics somehow. For example, in Python, we have… we found a way with the site customized script.
To, to check.
the version of Python before we try to inject it, because if we injecting 2.7, it goes like, poof.
Same also 3.1.
Stuff like that.
And the third one is that, it must support declarative configurations. And the last one is what, is, preventing us from making a Ruby package. There is work happening in the Ruby SIG.
The moment Ruby has the clarity configuration, we'll make a package for Ruby as well.
And, I think I would like a co-author for the, the OTAP that I promised to write in the last container call about what it takes for a language to be automatically injectable.
Because people in the project, they don't know what it means.
**Antoine Toulme (Splunk Inc.)** 32:05 Yeah, makes a lot of sense.
Okay, that's an inject a SIG discussion, maybe.
Hmm.
**Michele Mancioppi (Dash0 Inc.)** 32:11 Very much a packaging album.
The injector is concerned only With, the, Setting the environment variables. But, for example, the criteria configuration is a decision on the packaging level.
**Antoine Toulme (Splunk Inc.)** 32:26 Yeah.
Take care.
Love to help, but… yeah.
Emil.
Right, I gotta run, might not be at the injector SIG guy, I have a conflicting meeting, but… Enjoy.
**Michele Mancioppi (Dash0 Inc.)** 32:51 Alright.
