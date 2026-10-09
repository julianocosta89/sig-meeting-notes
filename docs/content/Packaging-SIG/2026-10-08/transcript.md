SIG: Packaging SIG
Date: 2026-10-08
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Denys Sedchenko** 01:12 It's…
**Michele Mancioppi (Dash0 Inc.)** 01:23 Hello.
**Denys Sedchenko** 01:25 Hello guys, how are you?
**Michele Mancioppi (Dash0 Inc.)** 01:30 It's already pre-Kubecon season as far as I'm concerned.
**Diego Hurtado (Dash0)** 01:35 There he is. Let's go ahead.
**Damien Mathieu** 01:37 Hi.
**Michele Mancioppi (Dash0 Inc.)** 01:38 Hi.
Oh, welcome!
**Diego Hurtado (Dash0)** 01:45 Yeah, welcome.
**Michele Mancioppi (Dash0 Inc.)** 01:51 Let's wait maybe a minute for maybe Antoine to show up.
**Denys Sedchenko** 01:57 Michele Damien.
**Damien Mathieu** 01:59 just.
**Denys Sedchenko** 01:59 Fill your name in attendees.
**Damien Mathieu** 02:03 Oh, yes, sorry.
**Michele Mancioppi (Dash0 Inc.)** 02:18 Oh, there he goes.
**Antoine Toulme (Splunk Inc.)** 02:26 That's me.
**Michele Mancioppi (Dash0 Inc.)** 02:30 All right, folks.
I we have been. We have a few Prs on the Packaging OpenTendry Packaging Repository. I'm going to share the screen.
Oh, hi, Ted.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:52 Hello, hello.
**Michele Mancioppi (Dash0 Inc.)** 02:55 This PR by Diego, I need to look at again.
It looks correct, but the last time I looked at it, it did not.
It was generally in the right direction, but… It was not yet passing CI, so I'll have a look.
**Diego Hurtado (Dash0)** 03:16 It is.
Yeah, it is now.
**Michele Mancioppi (Dash0 Inc.)** 03:19 Now it is, but I still need to look at it again.
**Diego Hurtado (Dash0)** 03:22 Oh, sure, I mean… Look at it, just to give you some context.
We've been working on this issue about calculating the minimum Minimum Python version, right? For… for site customize. So we grab all our dependencies, and we the… Calculate what Python version.
They need for all of them to work.
And, I realized yesterday that There is one particular dependency.
that, it's been compiled.
Or has a compiler part, sorry.
That only works on 3.11, so… That dependency is needed for config files, so right now, as things are.
config file.
Packaging and Python can only work on 3.11. No more, no less. So we need this to… To move the… Forward, yeah.
That's it. Thank you.
**Michele Mancioppi (Dash0 Inc.)** 04:34 Which means we also have a gap in our validation, right?
**Diego Hurtado (Dash0)** 04:40 Validation of what?
**Michele Mancioppi (Dash0 Inc.)** 04:42 We, the… when we updated Pi, the Python distro.
With, through Renovate, that did not trip any test.
**Diego Hurtado (Dash0)** 04:53 The… Probably because it wasn't testing the specific case of configuration files.
**Michele Mancioppi (Dash0 Inc.)** 05:04 Yeah, certainly.
So it's worth to add tests for configuration files across all the languages.
**Diego Hurtado (Dash0)** 05:11 I think this one, this one does, yes, just… But in any case, you can take a look and…
**Michele Mancioppi (Dash0 Inc.)** 05:18 Yeah, if you can also add the… so as a follow-up PR, So I'll look at this today or tomorrow.
And, open follow-up PRs for the other languages as well, where we exercise.
The configuration file path.
**Diego Hurtado (Dash0)** 05:34 Okay.
Alright, yeah, makes sense. So that's… We're also testing that. Okay, I'll do it.
**Michele Mancioppi (Dash0 Inc.)** 05:44 The Ruby Auto Instrumentation package is blocked on Ruby supporting declarative configuration.
I… I believed I had.
Made a comment.
Oh,
**Antoine Toulme (Splunk Inc.)** 06:06 BLA, Agreement cancels 7.
Yeah.
**Michele Mancioppi (Dash0 Inc.)** 06:19 Welcome.
**Antoine Toulme (Splunk Inc.)** 06:21 Is it?
I'll find him.
**Michele Mancioppi (Dash0 Inc.)** 06:29 Yeah, I believe I made the comment on the issue, not on the PR.
**Antoine Toulme (Splunk Inc.)** 06:36 No, it makes sense.
**Michele Mancioppi (Dash0 Inc.)** 06:44 This, The cyclone… Bomb, I am.
I'm not quite sure it is the best format for us.
And I am not aware of… Policies around this.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:10 Sorry, what's the question?
**Michele Mancioppi (Dash0 Inc.)** 07:13 Do we have preferences at the level of the project?
In which format?
We model bill of materials.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:22 I don't think we do.
**Michele Mancioppi (Dash0 Inc.)** 07:25 Do you think we should have preferences?
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:34 I mean, like, should we be using JSON?
I think it should be structured, certainly.
**Denys Sedchenko** 07:43 Can we use SPDX? Because this is the most common format I saw.
**Michele Mancioppi (Dash0 Inc.)** 07:49 I would like to… so, in my opinion.
No, it's not even an opinion, but I would kind of expect this discussion to have taken place at some point during the stable by default discourse.
Because bill of materials are a thing for enterprises.
And, the correct format is whatever everybody else in the project uses, right?
If anybody does.
**Antoine Toulme (Splunk Inc.)** 08:16 I'm not aware that the collector does anything around, Bill of materials type things.
It's interesting.
Cyclone DX is a well-known format.
**Ted Young (Raintank, Inc. – Grafana Labs)** 08:31 Yeah, I don't think we have this concept in OpenTelemetry at all.
**Antoine Toulme (Splunk Inc.)** 08:36 I mean, I've… We have… Michael is right, like, in my function as, you know, with working with customers, we send them bombs all the time.
I don't know, what's the alternative to this format?
**Michele Mancioppi (Dash0 Inc.)** 08:55 Hey, Dean.
**Denys Sedchenko** 08:57 SPDX.
**Antoine Toulme (Splunk Inc.)** 08:59 Which one do you folks want to support?
**Michele Mancioppi (Dash0 Inc.)** 09:02 I don't believe we should take this decision among five of us on a Thursday afternoon. I think this is something that…
**Antoine Toulme (Splunk Inc.)** 09:10 Okay.
**Michele Mancioppi (Dash0 Inc.)** 09:11 This is what the technical committee owns.
**Antoine Toulme (Splunk Inc.)** 09:13 Would you like us to chalk that up to the TC?
Or… Do we have to choose? Can we not do both?
After all.
What's another?
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:31 Doing a, yeah, doing a quick search, you know, I see there's, you know, OpenTelemetry Java as a concept of a bomb.
**Antoine Toulme (Splunk Inc.)** 09:40 Okay.
But you probably get the bump for free with Maven at this point.
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:46 Yeah.
**Antoine Toulme (Splunk Inc.)** 09:54 Alright.
I vote we do both, unless we're told that one is better than the other.
**Michele Mancioppi (Dash0 Inc.)** 10:07 I mean, we had it here, right?
**Antoine Toulme (Splunk Inc.)** 10:22 I see.
**Michele Mancioppi (Dash0 Inc.)** 10:35 So that one, please somebody bring it to the TC.
I believe we should have…
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:41 Next week's spec meeting as well. Bring it up there.
**Antoine Toulme (Splunk Inc.)** 10:45 Thank you.
**Michele Mancioppi (Dash0 Inc.)** 10:47 I am not sure I will be able to attend. Actually, I'm pretty sure I will not be able to attend.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:55 Okay.
**Michele Mancioppi (Dash0 Inc.)** 10:55 But please don't block on me not being there.
I do not have a horse in this race. I believe we need to have a bomb, and we should be consistent across the project, and that's the extent of my opinions.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:09 It should open an issue and then.
**Antoine Toulme (Splunk Inc.)** 11:14 Yeah, that would be in community, or…
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:18 That's a good question, whether something like that would be in community or in the spec repo.
**Michele Mancioppi (Dash0 Inc.)** 11:25 I believe there will be a requirement for libraries, distributions.
Packaging, and that lives in, specs.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:32 I think I would agree that it seems like it's a spectrum.
**Michele Mancioppi (Dash0 Inc.)** 11:35 Nobody.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:36 Packaging.
**Antoine Toulme (Splunk Inc.)** 11:37 Specification.
Let me see… Just reviewing the existing issues.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:49 Yeah.
**Antoine Toulme (Splunk Inc.)** 11:54 Nothing about SPDX, anything.
Hmm.
Nothing matching Cyclone.
Nothing about bill of materials. It's never been asked.
Dad, do you want to end up opening the issue?
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:18 Yeah, I can do that.
**Antoine Toulme (Splunk Inc.)** 12:19 Okay, cool. Thank you.
**Michele Mancioppi (Dash0 Inc.)** 12:22 This PR is in draft.
**Diego Hurtado (Dash0)** 12:26 Right, that's fine. I'm… Moved it to draft, because I need the other PR that I showed you.
To be immersed first.
**Michele Mancioppi (Dash0 Inc.)** 12:37 So, you need 148.
**Diego Hurtado (Dash0)** 12:40 That's right. Yeah, please.
**Michele Mancioppi (Dash0 Inc.)** 12:44 Okay.
Can you stack them? Do we have access to stacked PRs in this org?
It makes the merging so much faster.
**Antoine Toulme (Splunk Inc.)** 12:54 I think so.
I tried, I tried it, it just was a lucky mail attempt.
**Michele Mancioppi (Dash0 Inc.)** 13:05 This PR, I owe you a second round of reviews, I believe, Antoine?
**Antoine Toulme (Splunk Inc.)** 13:12 Yeah, whenever you have time.
**Michele Mancioppi (Dash0 Inc.)** 13:14 it's… So.
Oh, look at it!
**Antoine Toulme (Splunk Inc.)** 13:18 Also, others, feel free to chime in.
**Michele Mancioppi (Dash0 Inc.)** 13:24 And this one.
I, this one, I need to look at again.
the, I don't necessarily believe on.
Static checks at post-install of the package.
But I no longer remember, Diego, what you tried with this PR.
**Diego Hurtado (Dash0)** 13:59 Yeah.
That's, that's an old one, I am.
Okay, let's do something. I'll… I'll take a look again.
This pair… And, I'll make sure if draft is the right state.
**Michele Mancioppi (Dash0 Inc.)** 14:23 That's good.
And then we have a new repository in the SIG, and that's the Homebrew tab.
Has no people requests, but one open issue, and that is the classic dependency dashboard.
Damien, do you want, to give us an update of what you think we should be doing next in this repo?
**Damien Mathieu** 14:51 I mean, it's working. We have OCB there. I've seen, requests to add other things, such as a collector.
We can start adding VATs. Technically, so, for the starting required.
Things for here, it is technically done.
Yeah, I mean, if anyone wants to work on starting a collector.
Brew, feel free to do so.
**Michele Mancioppi (Dash0 Inc.)** 15:27 I believe that… The RITMI is a bit anemic, especially in terms of the goals and the scope.
For example, Is it targeted both Linux and Mac?
Something that we should state.
**Damien Mathieu** 15:47 Sure.
**Michele Mancioppi (Dash0 Inc.)** 15:48 With system packages. At the moment, there isn't one.
**Damien Mathieu** 15:54 Sure, maybe, can we just open an issue now to track what we want to add there?
**Michele Mancioppi (Dash0 Inc.)** 16:00 Sure.
**Damien Mathieu** 16:19 Feel free to assign that to me.
**Michele Mancioppi (Dash0 Inc.)** 16:41 Yeah, well, you know, I'm very happy about the addition of Homebrew Tap.
At some point, I'll probably do something stupid and propose starting NixOS packages, because It is a guilty pleasure of mine.
**Diego Hurtado (Dash0)** 16:58 That's stupid, really.
**Antoine Toulme (Splunk Inc.)** 17:01 having.
**Diego Hurtado (Dash0)** 17:02 Waiting for that.
**Michele Mancioppi (Dash0 Inc.)** 17:03 Remember that next week we are going to be in the same room.
**Diego Hurtado (Dash0)** 17:08 Alright, something is gonna… come up.
From that.
**Michele Mancioppi (Dash0 Inc.)** 17:13 Not speaking.
**Diego Hurtado (Dash0)** 17:14 Good or bad, maybe, but something's happening.
**Michele Mancioppi (Dash0 Inc.)** 17:17 No, there is a fantastic support for the collector on NixOS, and I am going to plug, a shameless… An absolutely shameless self-plug.
Because I wrote an article about it, I was really impressed with the quality of it.
**Antoine Toulme (Splunk Inc.)** 17:38 I was about to send you a trace correlation article to my engineering team.
**Michele Mancioppi (Dash0 Inc.)** 17:42 Thank you. So, I wrote an article on LinkedIn articles, which probably two people, and one is me, has read, but the quality of the support in XYZ is really cool. You can really do Very cool stuff.
It's really, really good.
**Diego Hurtado (Dash0)** 17:58 You're impressed with the quality of the support, or the quality of the article?
**Michele Mancioppi (Dash0 Inc.)** 18:03 According to the support. The article is excellent, but according to the support, it's fantastic.
**Diego Hurtado (Dash0)** 18:09 Alright.
**Michele Mancioppi (Dash0 Inc.)** 18:12 Which brings us, I believe, to next topic of improving the quality of the support of the packages with OCB and the packages. Denis, do you want to take it over?
**Denys Sedchenko** 18:25 What needs to be done…
**Antoine Toulme (Splunk Inc.)** 18:30 So we got Cloudflare access, that's great. Did you all get access to your Cloudflare account? Are you all in there?
**Denys Sedchenko** 18:37 Yeah, I have an access, but the problem is that's the only thing I have.
**Antoine Toulme (Splunk Inc.)** 18:43 Exactly. There's no domain setup.
**Denys Sedchenko** 18:47 Not just domain, I… just to get… start to get, like… Just to get start working, I need the copper project or copper account.
We can, like, someone can just create, like, with admin, with access to admin at OpenTelemetry IO can just, like, create an account and create a project and just give us a permission.
**Antoine Toulme (Splunk Inc.)** 19:12 you.
**Denys Sedchenko** 19:12 That's all we need.
**Antoine Toulme (Splunk Inc.)** 19:13 That's… Can we ask Ted for this? Would that be the right person to do it? I think… He's the right person, but…
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:24 I mean, I think you do want to open a community issue for this.
**Antoine Toulme (Splunk Inc.)** 19:29 That's right, I have a community issue open for this.
It's not going the way I'd like, because I think I asked for too many things in one issue.
But it's here.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:43 Yeah.
**Antoine Toulme (Splunk Inc.)** 19:44 Where'd I put it?
I was just on that.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:53 But…
**Antoine Toulme (Splunk Inc.)** 19:54 I'll find it. Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:56 That is actually a great point. I've definitely noticed, like, community issues. If it's, like, a very specific ask, like, it's a lot easier just to get it done.
**Antoine Toulme (Splunk Inc.)** 20:04 Amen.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:05 A couple of things and some questions, then it's harder to get things resolved, for sure.
**Antoine Toulme (Splunk Inc.)** 20:13 So one thing is okay. Two weeks ago, there is a message here from Trask, which I think is interesting.
He said, if you need a single email for it, I'd suggest setting up Packaging-Maintainers at OpenTelemetry.io Google Group.
Your GC liaison can set this up.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:30 Okay.
**Antoine Toulme (Splunk Inc.)** 20:31 So, so… I don't know what that means, but… Very much puts you in a… in the driving seat of making that Google group work.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:44 Yeah, I can, I can make that happen, for sure.
**Antoine Toulme (Splunk Inc.)** 20:48 Awesome. So, if you can do that, then… Then we're in a good place, and we can use this as the email to sign up.
**Denys Sedchenko** 20:57 Thanks.
We also… Besides, like, signing into account, we also would need to create a… an API token.
And you do that by basically running the copper CLI locally and then basically storing that API token on CI.
I don't feel right to use my personal Hoppy token on Copper.
So maybe it's, like, also should be, like, a token created by the…
**Antoine Toulme (Splunk Inc.)** 21:28 Sure, yeah.
**Denys Sedchenko** 21:29 Our account.
**Antoine Toulme (Splunk Inc.)** 21:31 If I'm understanding correctly, what this is saying is, like, we would be getting a shared account under this Packaging Maintainers at OpenTelemetry.io.
So we can all.
**Denys Sedchenko** 21:41 For… for running this, like, for using… In GitHub CI, yes.
**Antoine Toulme (Splunk Inc.)** 21:47 Yes, but not locally. Yeah.
**Denys Sedchenko** 21:50 Yeah, yeah. Locally, like, we can just, like, opt, like.
like, everyone from the SIG will be invited into the project, and then everyone from the SIG can, like, modify the project if necessary, and, like, run stuff locally.
**Antoine Toulme (Splunk Inc.)** 22:04 Yes.
And then you would get the API token as a one-time thing from the logging as the packaging maintainers.
**Denys Sedchenko** 22:13 True, yeah.
**Antoine Toulme (Splunk Inc.)** 22:14 Okay, so… we just need the Google Group set up, then we're unblocked on copper, but, that would… that would give us what we need.
But then the next step is also… so on Cloudflare, I have some hesitations of what to do here, because… It's like… you know, took us 10 days to get access, now we're in, and now I find this to be pretty useless, because there's no domain setup.
Should I don't know how to ask nicely, or what exactly I need to ask, because it looks like Cloudflare requires you to have the top domain to be set up in Cloudflare.
Is that a correct assumption?
**Denys Sedchenko** 22:53 I can I can research that.
Like I know how it works on other clouds when you're trying to connect the bucket.
**Michele Mancioppi (Dash0 Inc.)** 23:01 But I, I thought the plan was to have it go through with a pass-through.
Through Netlify.
**Antoine Toulme (Splunk Inc.)** 23:09 No, Netlify has no… I researched, I mean, I don't know, maybe someone else has a different opinion, but I looked at Netlify, and it doesn't offer blob storage in the same way that Cloudflare does.
Demis.
**Michele Mancioppi (Dash0 Inc.)** 23:22 I know, I remember that, but that's why I said in pass-through.
**Denys Sedchenko** 23:28 Okay, yeah, yeah.
**Antoine Toulme (Splunk Inc.)** 23:28 you.
**Denys Sedchenko** 23:29 If we have a blob storage in a separate location.
Doesn't matter what provider you have. Cloudflare, S3, whatever. Yeah.
Like.
You want to basically… You usually have a load balancer.
Sorry, not basically have a like you have a basically have a proxy.
But basically, when you access to packages, telemetry I/O.
It basically proxies request the blob storage.
And also it's managing the SSL question, basically SSL certificates.
So, we just… we just need the… Basically, we just need, like, that kind of proxy.
Maybe Netlify offers something like that, that basically it will just proxy the request to the blob storage.
**Antoine Toulme (Splunk Inc.)** 24:35 We didn't look at that.
But can you even create a blob storage without a domain setup in Cloudflare? I didn't see an option to do that.
**Denys Sedchenko** 24:45 You usually first create a separate blob storage, and then if you visit the Cloudflare, you attach it to a particular domain. But you can create a blob storage without actually like attaching to a particular domain.
**Antoine Toulme (Splunk Inc.)** 24:59 Okay, alright, I'm checking that.
So, that's there.
Sorry, just a sec.
So, so, can we… can we try and do that right now?
**Denys Sedchenko** 25:29 Yeah, just give me a second, this was what I'm trying to do.
**Antoine Toulme (Splunk Inc.)** 25:33 Yeah.
**Denys Sedchenko** 25:35 Okay…
**Antoine Toulme (Splunk Inc.)** 25:38 object storage type thing.
**Denys Sedchenko** 25:42 Yeah, yeah, it's called Cloudflare R2.
**Antoine Toulme (Splunk Inc.)** 25:45 Okay, I see it.
**Denys Sedchenko** 25:47 But… I can't remember what it says.
**Antoine Toulme (Splunk Inc.)** 25:51 Let's see three options.
**Denys Sedchenko** 25:53 Okay.
What's something for me? What's…
**Michele Mancioppi (Dash0 Inc.)** 26:00 Folks, before we run out of time.
There is, A couple of topics open. One is… We are not making progress with bringing the collector package into the fold.
And I do not remember if we made that a goal for the… For the short term or not.
**Antoine Toulme (Splunk Inc.)** 26:27 I don't think so.
I think I would be panicking otherwise, but let me… Review the community projects shorter.
**Michele Mancioppi (Dash0 Inc.)** 26:35 I had… it was not a committee project, but the request came up, and I opened an issue.
on the collector releases, and then I don't believe anything meaningful happened with it.
Recently, somebody went and asked if there is progress with that, because the experience of validating the packages that you're downloading is less than stellar.
**Antoine Toulme (Splunk Inc.)** 27:00 And.
Alright, so yes, I don't see it, and then… where is your issue?
Let me see.
Or is it with Sean releases? Is that showing? Are you sharing your screen? Yes.
So back in July 1, 5, 6, 1.
**Ted Young (Raintank, Inc. – Grafana Labs)** 27:40 So I have this packaging.
a Google group set up. You wanna just paste your emails into the chat so I can add you real quick?
**Antoine Toulme (Splunk Inc.)** 27:54 Yeah, sure.
**Ted Young (Raintank, Inc. – Grafana Labs)** 27:59 I could get that for all the maintainers.
I think Denny, you as well, right? Who else?
What else is a packaging maintainer?
**Antoine Toulme (Splunk Inc.)** 28:27 Denise, think you're it, right?
**Denys Sedchenko** 28:29 Yeah.
**Antoine Toulme (Splunk Inc.)** 28:31 Let's go.
**Denys Sedchenko** 28:31 By the way, regarding Cloudflare, I replied in our Hotel Packaging channel, I stumbled upon a blocker or more like on a paywall.
**Antoine Toulme (Splunk Inc.)** 28:51 So we need someone else to do these for us?
**Denys Sedchenko** 28:54 I assume yes.
It's, for me, button is blocked, because, like, I'm not the owner.
**Antoine Toulme (Splunk Inc.)** 29:02 I thought there was some additional thing to do. So, okay, so we need to ask Austin to go do it for us.
**Denys Sedchenko** 29:17 Or we have an option B.
We already have a Google Cloud infrastructure, right?
**Antoine Toulme (Splunk Inc.)** 29:25 We have no money in that.
**Denys Sedchenko** 29:27 Okay.
**Antoine Toulme (Splunk Inc.)** 29:28 Good, it's… If you really insist and try to get yourself a cloud infrastructure, per se, you're going to end up on Oracle Cloud.
That's what this.
**Denys Sedchenko** 29:38 Bye.
Okay.
**Michele Mancioppi (Dash0 Inc.)** 29:42 Okay, Antoine.
Can you please warn us in advance before you say things like this?
**Antoine Toulme (Splunk Inc.)** 29:48 I'm sorry.
**Michele Mancioppi (Dash0 Inc.)** 29:48 Raise myself.
**Antoine Toulme (Splunk Inc.)** 29:50 I'm sorry, it's… he had one minute left in meeting, and everything was going so well, and then I had to mention that.
**Michele Mancioppi (Dash0 Inc.)** 29:59 So, open topics, the collector, still flying in the air.
One more paywall in Cloudflare, and I am making asymptotically progress with.
Oh, God, I'm terrible at names.
Jerry from the Php. Sig for automatic instrumentation.
Php is vicious as a language, and we'll talk more about this in the… in Chapter 6.
**Antoine Toulme (Splunk Inc.)** 30:34 Cool.
**Michele Mancioppi (Dash0 Inc.)** 30:34 See you on the other side, folks.
**Antoine Toulme (Splunk Inc.)** 30:37 Do them.
**Damien Mathieu** 30:38 Thank you.
**Denys Sedchenko** 30:39 Bye now.
