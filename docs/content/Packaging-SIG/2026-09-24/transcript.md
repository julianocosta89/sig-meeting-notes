SIG: Packaging SIG
Date: 2026-09-24
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 00:41 Hey.
**Denys Sedchenko** 00:44 Hello?
**Damien Mathieu** 00:47 Hey.
**Denys Sedchenko** 00:52 Antoine, you have a very nice background.
Nice machine.
**Antoine Toulme (Splunk Inc.)** 00:57 Thank you. Is it on? Yeah, it's on. Cool.
Where is the Nordstruck again?
**Sina** 01:24 Hello, hello.
**Csaba Gy** 01:25 Kind.
**Antoine Toulme (Splunk Inc.)** 01:29 Okay, so, let's the Packaging… Ducks, okay.
Right.
Hey, Austin.
Thanks for joining.
**Austin Parker** 01:47 Thanks for having me.
**Antoine Toulme (Splunk Inc.)** 01:50 Alright, so we got this, doc here, we can put your name in if you want.
It's always cool.
Agenda… We'll take some notes in here.
And, we're joined today by Austin, who is going to help us understand a little bit more how we go about this whole infrastructure for packaging, right? So, I think that's going to be a very nice conversation. Thank you for joining, Austin. We appreciate you taking the time.
Okay, so maybe let's dive in. More people will join as we go.
I ended up in an issue a couple weeks ago.
Related to having some sort of infrastructure that we could work with here.
Context, this issue is under community.
Issues… No fur.
So, back edging infrastructure.
It's a little difficult to unwind, because the problem we're having is that we are trying to get access to infrastructure, but at the same time, we would like very much to, be inside, you know, in lockstep with the proper best practices of OpenTemmetry, so that, first off, we don't want to go, you know, wild and get our own accounts. We should make those OpenTemmetry-backed, managed, properly maintained.
So I think there's a process here, and, you know, there was an infrastructure SIG for a while, but you guys stopped meeting because there was less going on.
So we used to have an avenue, but we don't have an avenue anymore, and that's okay. Maybe it's better to discuss it here.
And the other is the choice of technology you want to use. So… We've identified that, with copper, we can get all the RPM needs fulfilled.
We would like to also do a good job of, understanding how to… how to use some sort of S3-like storage, so that we can store, all the artifacts we have in mind, and make it easy for ourselves to serve them at scale, like, behind a CDN of some sort.
And Cloudflare came to mind, especially for Denys. I think you… did you go all the way to testing Cloudflare? Did you actually set that up?
**Austin Parker** 04:11 Oh.
**Antoine Toulme (Splunk Inc.)** 04:15 Glided.
**Austin Parker** 04:18 We have, so we have…
**Antoine Toulme (Splunk Inc.)** 04:22 I think it's a funny…
**Austin Parker** 04:24 Yeah, no, it's put us on stage together. So I was gonna say, just to let you know, we have an OpenTelemetry Cloudflare account, and I forget the exact amount of credits they've given us, but it's a lot.
And if we need to add people to that, I can totally do, and give you all a space to do your stuff in to access R2. I can totally do that, I just need to know like… Who I should invite.
**Antoine Toulme (Splunk Inc.)** 04:50 Okay, that's… that's a good list. We can give you all the maintainers of the SIG? Would that probably be it?
Okay. No, that's helpful, but next, I would like you to also delegate NS record to packages.upentimetry.io to that Cloudflare account. Is that possible?
**Austin Parker** 05:08 Yeah, that's… should be totally doable.
**Antoine Toulme (Splunk Inc.)** 05:11 And then… Denys, go for it.
This is your… this is your moment.
**Denys Sedchenko** 05:16 Thanks.
First of all, Cloudflare is not a hard requirement. We can swap it with anything else, but… There is a certificate, moment, so… I might not know everything, I'm just telling from what I saw from outside, I assume Netlify manages our SSL, is it right?
**Austin Parker** 05:42 Yeah, we use Netlify to… I mean, it's through Let's Encrypt or whatever, but…
**Denys Sedchenko** 05:50 Okay.
Then, what I saw, like, at least in the browser, Netlify ships a wildcard certificate.
But, like, let's assume we will pick any other S3 compatible storage. For example, it could be AWS, yeah?
We can have a bucket, but we also would need an SSL, because if you just, like, make a CNAME to the bucket, it's not going to work, because cell certificate is different from what AWS provides, so we need a load balancer in front that will basically stamp a correct, SL certificate.
With SSL certificate, okay, we can try to issue one. As far as I know, AWS allows to do that.
But it also… but it will have a conflict with the SSL certificate… wildcard certificate, which is used on OpenTelemetry I.O.
And, when I checked, basically there is a restriction on, like, on issues, issuers. So, like, one of the allowed issuers there is a Google one.
And, it means that it should be the Google bucket. Like, I know we have a Google Cloud account.
So…
**Austin Parker** 07:15 Yeah…
**Denys Sedchenko** 07:15 I can replicate the same setup, basically, with, Google… Google.
**Austin Parker** 07:20 Okay.
**Denys Sedchenko** 07:20 Google Bouncer.
**Austin Parker** 07:22 So, here's the story with that.
the Go SIG… Go SIG uses a Go vanity URL… uses a vanity URL through some Go thing that was set up on GCP, like, forever and an age ago, and… is still on GCP, but that's why… GCP can issue stuff under, the hotel… Under OpenTelunder.io, there's some… It's like, go.opentelemetry.io is the A record, and then… I think what it is, I think we have multiple… Yeah, so what it is, is that… OpenSummit.io has multiple CAA records?
For Let's Encrypt.
So, one of those is Google, is GCP's, Acme issuer, another is Netlify's. If, for whatever reason, like.
we needed Cloudflare to issue as well, then we could add a CA record for Cloudflare's Let's Encrypt account.
**Denys Sedchenko** 08:38 Okay.
The CIA was basically my concern.
**Austin Parker** 08:43 Yeah, you can have multiple CAAs on a, top-level domain, on an APEX domain.
Nice. Which was news to me, but apparently that's how it works, so… yay.
**Denys Sedchenko** 08:55 Yeah.
If we can control CAA, we can pick up whatever solution it was.
for Cloudflare, like, for my POC, I picked up the Cloudflare, first of all, because it's very easy to set up, and plus, I could have a free ingress.
**Austin Parker** 09:10 Yeah.
So what we can do… Okay… Looks like… So it looks like I… actually, weirdly enough, do not have Super Admin on this, so I will need to… Request it… But once we do that, we can get the maintainers of this in a group, And then… Y'all can go to town.
**Denys Sedchenko** 10:01 I have a question. What mechanism do you use? Like, for example, in GitHub workflows, I would need, obviously, to have credentials to upload stuff to S3.
And also… I would need a token… for, for Copper to do uploads, how do you, like, provision the secrets? Do you just use GitHub secrets, or you have some kind of a middleware in terms of, like, like a vault or something like that?
**Austin Parker** 10:29 I think we… I mean, we have a 1Password account, but I don't think it's wired into CI anywhere, so we just use GitHub Secrets.
And store the secret in 1Password, and then copy it into GitHub.
**Denys Sedchenko** 10:45 Okay.
So, meanwhile, infrastructure… so, like, what's the proper way to actually get the ball rolling? Maybe first to get an account for, like, get an email account.
And clean.
**Austin Parker** 10:59 the copper.
Well, I don't… so I didn't… the part of this I'm unfamiliar with is copper. Can someone… Quickly bring me up to speed on that.
**Denys Sedchenko** 11:10 Okay, so Copper is basically… basically, it's a service from Fedora that allows you to build packages for Fedora on their side.
And also to generate the repository.
the RPM repository. It also manages the GPD, key, so we don't need to manage it. It basically signs the packages, signs the repository metadata.
Basically, in our GitHub workflow, I basically triggered the job, Job.
makes, like, a copper on its side, makes Git pull, builds the packages, generates the repository.
Then the plan is, after the build is finished, I basically copying the repository method, the repository into our blob storage into our bucket.
**Austin Parker** 12:07 Okay.
So what… Yeah, so it sounds like… Do you need… Like, so for the email, I guess a good question is, is… Poor copper… Presumably, you would want the account for that to be an OTEL, like an OpenTelemetry account?
**Denys Sedchenko** 12:33 Yeah, it should be an official one.
And, like, account will be used for me, basically, to log in, create a project, set up the project, set up the runners I actually need.
**Austin Parker** 12:45 Yeah.
**Denys Sedchenko** 12:45 on CI's side, You authenticate using a token, which you obviously also need to create on, like… It's created when I, like.
when I use a Copper CLI, when I log in with a Copper CLI, it populates me a token, then I basically copy that token, and create it as a GitHub secret, and use it, and then use it.
**Austin Parker** 13:09 How… How much, like, on… On a recurring basis, like, how often do you think a maintainer from this SIG would need to be able to log in interactively to Copper?
**Denys Sedchenko** 13:28 Right now, basically, during the process of setup.
Right now, I needed to be able to log in for some time, and… Maybe later, if you need to figure out is something wrong, or maybe you need to modify the runners that you want to run in, basically, the maintenance of the project, or if you need to edit the project metadata.
**Austin Parker** 13:51 Yeah.
I'm… yeah, my… I'm… I guess my… my… what I'm trying to think of in my head is, like… Should we create a, like, packages at opentelemetry.io?
Because right now we have admin and OpenTelemetry I.O.
But I don't necessarily want you guys to have to, like, go through the GC every time you want to do anything.
Ted, what do you think?
As other person with keys to this.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:22 I mean, I… I'm generally a big fan of… you know, keeping the things locked down, especially… I mean, something like this, right? Like, someone gets access to copper, it means they can…
**Austin Parker** 14:40 Yeah.
Right. Yeah, no, a big, big bad, yeah.
But also, admin kind of has access to, like, all OTEL stuff.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:52 Sure, I mean, it… sure. But, like… I mean, we could refactor admin, that would be another thing we could look at. But, at any rate, like, the downside of having an email account that the Packaging SIG can't access to is that you have to bother someone who's an admin when you need, like, an email verification. That's… that's, like, the basic annoyance.
As long as that's not too terrible, I think… Not giving out access to that email account is wise.
we could have multiple email accounts, right, that are sharded, and then we don't give out access to them, but the question is, like, do we have an email account that we give out access to or not? And I think not is… ideal.
**Austin Parker** 15:47 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:49 If it's not too annoying, because you very rarely have to get in there. And you don't have to get in there for emergency reasons.
Danny, what do you think?
**Denys Sedchenko** 16:02 Also, like, During setup, I might need to… Login to email multiple times, especially.
**Austin Parker** 16:10 Yeah.
**Denys Sedchenko** 16:10 process, and, like, I don't want to ping someone We can change the owner later. Basically, we can change your email.
if necessary, maybe… I'm not sure yet, but maybe the project, like, maybe COPR has some kind of, like, way to basically, like, have collaborators, or, like.
multiple accounts that have different level permissions. I'm not aware, because I didn't use that, but I assume it might.
be possible.
**Austin Parker** 16:40 I mean, that would be ideal.
**Denys Sedchenko** 16:41 Fedora… yeah, because Fedora is using it to build its own, repository. Like, it's the thing that actually Red Hat is using.
**Austin Parker** 16:51 I think, yeah, I think Perfect World, we sign up as admin at, and then can add… You, or whoever… Like, temporarily, to kind of do all the setup, and then if we need… and then later we can, like, remove that, or, like, take… bust you down to, like, a viewer or something, just with the ability to kind of break glass and, like, re-elevate if we need to. That…
**Michele Mancioppi (Dash0 Inc.)** 17:17 That seems like.
**Austin Parker** 17:18 The best option?
**Michele Mancioppi (Dash0 Inc.)** 17:20 I would not be opposed to having a packages.top.io, so that we don't need to go and break a lot of stuff, because ultimately, I mean, the maintainers are trusted with changing the source code in GitHub.
Having to escalate to go and change the configuration of copper.
Yeah.
**Austin Parker** 17:39 Well… The only down… not even downside, just the only thing… the only reason I bring up, like, separate thing is just that I'm… Pretty sure that… the way email works is that we have to pay for each unique user on the OpenTelemetry domain.
And so, we would need to go back and, like… tell the CNCF that, hey, we're adding another user, or however many users to this.
Which is probably fine, I think it's, like, 8 bucks a month or whatever, but I just don't know if we can do that ourself, or if we have… like, I don't know if we can do that without going and, like, saying, hey, we're gonna do this… Right, I just don't know how quickly… That could take, or happen.
**Denys Sedchenko** 18:27 Is there an existing email that we can reuse? Does the pack… like, we have, like, a…
**Austin Parker** 18:33 Admin…
**Denys Sedchenko** 18:34 Google groups.
**Austin Parker** 18:36 admin at would be the existing one that we would reuse, which is what we've been tending to use for everything, like, we've… Everything gets admin at.
**Denys Sedchenko** 18:52 Yeah, and asking access to admin would be too much, because it's, like, account for.
**Austin Parker** 18:56 Yeah, no, we can't… Admin Ed is strictly GCTC. So that's kind of the thing, right? Like…
**Antoine Toulme (Splunk Inc.)** 19:11 Well, we do both…
**Austin Parker** 19:12 Can you figure out if… I mean, I think a good option, you know, something we can figure out pretty quickly, probably, is does Copper let you create, like, an organization and then delegate to another person, right? Could we create the Copper account As admin at, and then add you with whatever email, and have you be, like, an admin on it.
So that you can go do all the setup, you know? And, like, we don't even have to, like, restrict your access later, like, to… to the point earlier about, like, maintainers… yeah, like, I'm not saying… like, Michele, we don't have to, like, remove ad maintainer access from that team.
Unless we… unless you all thought that was a better plan.
But I think the owner of that account should be an OpenTelemetry… Like, at OpenTelemetry.
**Michele Mancioppi (Dash0 Inc.)** 20:02 I agree.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:02 Yeah, and it's helpful for that to be admin. Let's just double-check if you can have multiple, I'm sure you can. It's helpful to have admin on there because it makes it also easier to get To kind of, like, track…
**Austin Parker** 20:16 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:16 Logging alerts and various other things, right?
**Austin Parker** 20:19 It also makes continuity much easier for GCTC.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:24 Yeah.
But I think it's reasonable to find… I don't know, we don't have a lot of situations coming up where maintainers need, like, email access to things.
So we don't have a good solution to that right now.
But… why don't we just start with admin, and then start by adding some of the maintainers directly, and… and just see how that goes.
the… Problem is it just means you have to remember to remove those maintainers later.
But we could take that as, like, a community action item to figure out what a better… a better solution is without blocking the SIG by doing it that way.
**Antoine Toulme (Splunk Inc.)** 21:14 Okay.
**Austin Parker** 21:17 Yeah, for my part, I'm… trying to… I'm… Trying to figure out how to get the… Cloudflare thing… Sorted out, but for whatever reason… Chad, I asked in chat, do you know, did they do something at the Service Desk?
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:38 I remember…
**Austin Parker** 21:39 do Service Desk anymore?
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:41 I've not logged into Service Desk recently, is it moving to LFX in somewhere?
**Austin Parker** 21:44 I didn't… that's what I don't know, like, I just logged in, there's no, like, ticket option, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:52 entirely possible that it's moving to LFX.
**Austin Parker** 21:55 Yeah, let me ask…
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:56 Like every other move to LFX, it's come as a surprise.
**Austin Parker** 22:00 Oh… it's with the… It's something with the maintainer's list.
**Denys Sedchenko** 22:28 By the way, I signed up into Fedora.
I see there is, There is a way to add collaborators.
like… At least they see it.
Like, you can grant permissions.
But, like, like, yeah, it's opt-in feature.
Like, after, like, user asks the permission, You… Ask, like, you as an admin has to approve that.
If someone has… Free time available.
If you can navigate here, and, like.
Can you open, like, please, can someone else please open the page, maybe, like… Sign up and tell whether, like, he can ask.
for permissions, Because I cannot add someone. As I understand, someone has to request adopt permissions.
I'm like, I should approve that.
Because I cannot grant permissions directly.
**Michele Mancioppi (Dash0 Inc.)** 23:40 Yeah, give me a second.
**Antoine Toulme (Splunk Inc.)** 23:43 Let me try.
**Austin Parker** 24:23 Well, just as a FYI, there appears to be some glitch in our service desk permission, so we are working on that, but as soon as I get that sorted, then I will… If someone just wants to message me on the CNCF Slack about… Who… should be.
**Antoine Toulme (Splunk Inc.)** 24:47 Do you want emails?
**Austin Parker** 24:49 Yeah, I need emails.
**Antoine Toulme (Splunk Inc.)** 24:51 Okay, so,
**Austin Parker** 24:55 If you already have, like, a Cloudflare account, then that email is good.
If you do.
**Denys Sedchenko** 25:01 Hi.
I have…
**Antoine Toulme (Splunk Inc.)** 25:12 I just don't have the email for Denis.
**Denys Sedchenko** 25:15 One moment.
**Austin Parker** 25:16 could just… Just politely…
**Antoine Toulme (Splunk Inc.)** 25:19 Please…
**Austin Parker** 25:20 Slack DM them to me,
**Antoine Toulme (Splunk Inc.)** 25:23 Ew.
**Denys Sedchenko** 25:24 Cynthia Austin.
**Austin Parker** 25:25 Thank you, yes, I see it.
I'll try to get it today, I don't know how quickly they're gonna… Respond.
**Antoine Toulme (Splunk Inc.)** 25:37 Yeah, okay.
Let me check… Oh, snowing.
Akita, your email still has 2M's, 1B, or two… Yeah, that right?
**Michele Mancioppi (Dash0 Inc.)** 26:15 Yeah, the other way around. One empty piece.
**Antoine Toulme (Splunk Inc.)** 26:19 I was so close.
**Michele Mancioppi (Dash0 Inc.)** 26:21 Jeez.
**Antoine Toulme (Splunk Inc.)** 26:23 Thank you.
Oh, okay. Alright, so I got this ring.
**Michele Mancioppi (Dash0 Inc.)** 26:29 Yeah, I'm trying to register on Copper, but I'm on mobile in the middle of Berlin, and it's not working.
**Denys Sedchenko** 26:36 Just wait.
**Antoine Toulme (Splunk Inc.)** 26:37 Yep.
**Denys Sedchenko** 26:38 Just wait a bit, it can be a bit slow.
**Austin Parker** 26:45 Well, I will… I'll work on getting y'all into Cloudflare so that you can start doing stuff, and then…
**Antoine Toulme (Splunk Inc.)** 26:56 Gotcha.
**Austin Parker** 26:59 Yeah.
**Antoine Toulme (Splunk Inc.)** 27:03 Yeah, it's Gucci on the pool.
**Michele Mancioppi (Dash0 Inc.)** 27:06 Denys, I, logged in.
No, wait a second, I need to log in again. Alright.
So, like, a bit of something.
Yeah.
**Denys Sedchenko** 27:22 And I sent you the… after you log in, I sent you the link that you should open. It's the permission step of the project.
**Michele Mancioppi (Dash0 Inc.)** 27:30 Yeah, I'm trying, but I need to adjust a couple of things. It's a problem between keyboard and chair on my side.
Well, I think I'm looking for.
**Denys Sedchenko** 27:46 And Austin, a question regarding CIA.
How hard to adjust it to add Cloudflare to CIA list?
**Austin Parker** 27:59 Probably pretty easy, player… Okay.
Yay!
Authorities…
**Michele Mancioppi (Dash0 Inc.)** 28:17 Okay, let me just stop it.
Nothing.
**Austin Parker** 28:44 We might have to…
**Michele Mancioppi (Dash0 Inc.)** 28:45 Dang.
**Austin Parker** 28:46 I might have to ping someone at Cloudflare about what their Let's Encrypt account is.
Or accounts. I don't know how many they have.
**Denys Sedchenko** 28:56 And then we would need to add a DNS record to Netlify, but that's probably after the… after the bucket is created.
**Austin Parker** 29:08 Yeah, I don't know the exact order of operations, but I assume… great bucket.
the bucket, and then we'll add the A record, or whatever, and then we'll add… or we'll add the CA record.
We'll add the A record, and then it should just work.
**Denys Sedchenko** 29:31 Yeah, because, like, every cloud provider has its own restrictions.
**Michele Mancioppi (Dash0 Inc.)** 29:35 Like…
**Denys Sedchenko** 29:36 Oh, your, like, your name of the bucket should contain a domain, or something like that.
I know Amazon has such kind of restriction.
Forget.
We need the load balancer in front.
**Antoine Toulme (Splunk Inc.)** 29:54 We're coming up to time, so what we're gonna do is, We're gonna continue this work, getting everybody in Cloudflare, everybody in Copper, make sure we got the permissions right.
I can't plug into Fidua today, it's just… it's just not winning.
And, thank you, Austin, for taking the time to come down and, you know, work with us on this. It might be an immediate action item is, We should document Cloudflare in the assets, MD, that can open an issue for that, or open a PR if you want.
**Austin Parker** 30:25 Yeah, CPR's great.
**Antoine Toulme (Splunk Inc.)** 30:28 Okay, appreciate that. And then we should list you as admin for Cloudflare, right?
Is that correct?
**Austin Parker** 30:33 Yeah.
**Antoine Toulme (Splunk Inc.)** 30:35 Cool.
**Austin Parker** 30:35 desk, too.
**Antoine Toulme (Splunk Inc.)** 30:36 Trust, too. Okay, so we'll do that, and we'll continue to work on this.
Yeah, thank you. Appreciate it.
**Austin Parker** 30:49 Alright.
**Michele Mancioppi (Dash0 Inc.)** 30:50 Bye, folks!
**Austin Parker** 30:52 Bye, buddy. Y'all doing great work.
**Antoine Toulme (Splunk Inc.)** 30:54 Thank you, Justin. I appreciate it.
