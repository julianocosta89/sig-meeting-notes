SIG: Packaging SIG
Date: 2026-10-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Denys Sedchenko** 01:52 Howdy, how are you?
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:54 Hey, how's it going?
I thought I'd be late, but it's just us.
**Denys Sedchenko** 02:01 Probably lots of people are busy.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:05 Nothing could be more important.
Yeah.
**Antoine Toulme (Splunk Inc.)** 03:35 Hello! Let's… Oh, Nicky days at his offsite, right?
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:42 Hello, hello!
Who's at an offsite? McKellie?
**Antoine Toulme (Splunk Inc.)** 03:47 Yeah, that's yours, too.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:49 The Dash Zero people?
**Antoine Toulme (Splunk Inc.)** 03:51 Yep. Gonna be quiet today.
Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:55 here.
**Antoine Toulme (Splunk Inc.)** 03:58 Well, how are you all doing?
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:02 Doing well. How are you doing?
**Antoine Toulme (Splunk Inc.)** 04:04 I'm feeling lazy today.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:06 Yeah, I'm actually not doing well. I'm recovering from being sick. I travel for a month, I don't get sick.
All over the place. I hang out with people who have kids for one day.
Solid.
**Antoine Toulme (Splunk Inc.)** 04:22 No, it's no escaping any of this stuff.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:25 Yeah.
**Antoine Toulme (Splunk Inc.)** 04:29 I'm sorry.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:32 I'm fine. I'm feeling better today.
**Antoine Toulme (Splunk Inc.)** 04:34 I believe in the back of a garage for a reason.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:37 Yeah.
**Antoine Toulme (Splunk Inc.)** 04:40 Okay.
But.
Denis, I guess, you made some progress on that PR for the… Copper support… I believe that both Miki and myself have access, maybe… Ted might be interested in having access as well.
And then what else? I think we need to finish this discussion about Cloudflare, right?
**Denys Sedchenko** 05:08 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:08 Yeah.
Also, did a little more digging into S-bombs.
**Antoine Toulme (Splunk Inc.)** 05:16 Oh, nice.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:16 So…
**Antoine Toulme (Splunk Inc.)** 05:17 How do you… Some feedback.
Let's actually open the docs, I guess.
Okay, alright, sorry. Again, very lazy today.
It starts with the S bomb.
**Ted Young (Raintank, Inc. – Grafana Labs)** 05:38 Sure. So, BOM, SBOM, different things. Java has a Java-specific concept of a BOM, but they don't actually produce an SBOM, in terms of the security software manifest we're thinking of.
that thing can be published. There's, like, two popular formats. The collector publishes one, OB publishes one.
And I think dot net publishes one.
The security SIG has been thinking about this.
**Antoine Toulme (Splunk Inc.)** 06:13 But…
**Ted Young (Raintank, Inc. – Grafana Labs)** 06:14 That SIG tends to think more about like guidance.
But I think it would be great.
to make a decision and add it into the spec, you know, at least under the guidelines for being packaged. I think it's reasonable for us to pick. But it did seem like the kind of situation where Picking… Picking something reasonable, Like saying, produce it in one of these two formats.
**Antoine Toulme (Splunk Inc.)** 06:45 Yup.
**Ted Young (Raintank, Inc. – Grafana Labs)** 06:46 And just leaving it at that as the first version would be probably fine.
**Antoine Toulme (Splunk Inc.)** 06:52 I like, I like.
Okay, so we were not… we're not buying into a particular path, we're just saying we're gonna do our best with what we have. So we could do… we could take whatever the PR is open right now.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:04 Yeah, OB publishes Cyclone DX. We could just double check whether the collector happens to do the same thing.
**Antoine Toulme (Splunk Inc.)** 07:15 I don't remember, to be honest, I don't… If it's something we publish, we do it as a… Bitmap.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:23 That would be… The only way I would go further is to mandate one or both.
formats be published, but I don't really know anything about these formats. There's just two that are popular.
But is it… if it's the case that, like, every tool knows how to parse both, then… You know.
**Antoine Toulme (Splunk Inc.)** 07:45 Yep. Obviously.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:46 Just pick the one that's easiest in your language.
**Antoine Toulme (Splunk Inc.)** 07:50 I see a SBOM file.json.
for the collector, and I think it's PDX. So they went with this PDX.
**Ted Young (Raintank, Inc. – Grafana Labs)** 08:03 So, they went with PDX?
**Antoine Toulme (Splunk Inc.)** 08:06 SPDX.
**Ted Young (Raintank, Inc. – Grafana Labs)** 08:07 SPDX, right, and OB does Cyclone DX.
So already in the two things we have, they do it two different ways.
**Antoine Toulme (Splunk Inc.)** 08:15 Let's see, should we just… When and if we repackage the collector, we should just republish whatever SBOM they have anyway, right? We should not try to come up with our own, that's a waste of time.
**Ted Young (Raintank, Inc. – Grafana Labs)** 08:27 Yeah, I was the it's just a question of like consistency.
Since they do it differently, the only consistency would be to say, everyone do it every way. Like, publish both formats.
**Antoine Toulme (Splunk Inc.)** 08:42 Let me, let me see that.
**Ted Young (Raintank, Inc. – Grafana Labs)** 08:44 I don't know if that actually has any value.
Otherwise, I would say everyone's just required to publish an SBOM somehow.
In the popular format of their choice, and just leave it at that.
Not mandate anything stronger.
**Denys Sedchenko** 09:01 In worst case, I assume both.
Formats are interchangeable, you can easily, like, convert one to another.
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:10 That… my impression was it kind of didn't matter. That's why there were two formats.
They have one out.
**Antoine Toulme (Splunk Inc.)** 09:17 Okay, alright, so the way it works in the collector is that when we make a release, we use something called GoReleaser, so we… that's why I don't know anything about it, because we use a tool that is kind of interfacing with the actual stuff, and it has a SBUM section, which itself calls another tool called SIFT.
Which itself… is available to… to have multiple output formats, so Cyclone DX, NSPDX, And whatnot.
So, one thing we could do is just ask the collector folks if we could have both, and… We could just say Cyclone DX is the one we want the most right now. I don't know.
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:58 Yeah. Yeah.
**Antoine Toulme (Splunk Inc.)** 10:01 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:02 Or we say, just do what you're doing, and… The next step up to… the thing that would pair well with, Some kind of requirement would be like a tool.
**Antoine Toulme (Splunk Inc.)** 10:18 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:18 But again, I feel like every language is probably, like, a different tool in each language to sort this crap out, right? Like, something that… reads a manifest.
Like, the package managers, like that, is my guess.
I'm tempted to just say the guidance right now is you have to publish one of these things.
**Antoine Toulme (Splunk Inc.)** 10:36 One of this is fun. Yeah, okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:37 We could be… we could say we prefer Cyclone.
If you don't care.
**Antoine Toulme (Splunk Inc.)** 10:43 Right. Start with Cyclone, and then the others. And so, we should merge that DR, is that what you're saying? Like, because… He's waiting for feedback, I guess.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:54 I don't think there's a PR that's ready to be merged.
**Antoine Toulme (Splunk Inc.)** 10:58 None of it's ready to be merged, but the whole reason we're having discussions is not because Who cares? Just, like, some random guy came over and… open a PR to say, hey, I'd like to see bombs for everything.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:13 Yeah.
**Antoine Toulme (Splunk Inc.)** 11:15 Let me see…
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:15 So, that, that… That was a PR? Okay.
**Antoine Toulme (Splunk Inc.)** 11:19 Let me see, let me check where it's at. Is it still open?
These things.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:24 Paul, it would be great to link that to this issue in the spec.
**Antoine Toulme (Splunk Inc.)** 11:30 I feel like…
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:31 I feel like the next step is to open a PR to the spec.
To… and this is kind of just the beginning of, like.
Getting more detail fleshed out in this section around.
Package management, packaging requirements.
**Antoine Toulme (Splunk Inc.)** 11:47 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:48 We just want to list.
In SBOM, in the popular format of your choice, we prefer Cyclone DX.
**Antoine Toulme (Splunk Inc.)** 11:55 Do you want me, I'm not gonna be doing a good job. Do you want me to do this right now with you on this call? We can take just 2 min, put the comments in the PA in the issue.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:07 I would say make your comments on the issue and then I'll open the PR. I, it's a.
**Antoine Toulme (Splunk Inc.)** 12:11 Oh, okay, alright, I got it, I got it.
Okay, so let me. Okay, we discussed in the packaging.
See… meeting… of 1015 and we have an open Pr.
a contributor… to, distribute.
Cyclone… The XS bumps.
here.
Is it pure?
We don't have a strong stance.
I just want to have at least one.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:58 Yeah.
**Antoine Toulme (Splunk Inc.)** 12:59 As… as bum.
We think it's okay.
to prefer Cyclone DX given the Given the community input at this time.
loads any other format is seems acceptable.
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:23 Because the collector doesn't support Cyclone currently, right? And we're not saying we're gonna block.
**Antoine Toulme (Splunk Inc.)** 13:29 It looks like…
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:30 Okay.
**Antoine Toulme (Splunk Inc.)** 13:31 like it's a matter of configuration in the tool that we use for release. So, if you want, we could do a follow-up where I go into the collector SIG and I say.
Do you mind if we publish both flavors?
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:43 Great.
**Antoine Toulme (Splunk Inc.)** 13:45 I… No one from the collector has… really spent that much time, as far as I can tell, thinking about it, so we are just going with defaults that are offered by the tool, so we can change our minds however we want.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:01 Nice.
Okay. Yeah, I think that's the follow-up question. Does it make sense to publish both formats? If because Mike, it seems like it's probably easy in most cases.
**Antoine Toulme (Splunk Inc.)** 14:15 It's just, like, we have a ton of files on that. You're gonna get some really generic feedback, like, Hey, we have 800 files.
Whenever we make a release of the collector today.
Are we about to get, like, 50 more files for just no reason? And… I can't say that I care one way or another.
So, yeah, it's okay, it's okay, it's okay.
Yeah, so… Let's, let's have you open the actual guidance, and then from there, I can go to Collector and say, hey, I think Cyclone DX is kind of winning the war. Do you mind if we push Cyclone DX?
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:52 Yeah.
**Antoine Toulme (Splunk Inc.)** 14:52 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:53 Yeah.
I mean, we're also maybe getting over-influenced by this, like, random one guy.
**Antoine Toulme (Splunk Inc.)** 14:59 Yeah, that's true, but I mean, I don't really get that much community input otherwise, right? So.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:04 Exactly.
**Antoine Toulme (Splunk Inc.)** 15:05 I'm gonna go where the wind takes me, yeah?
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:08 I think that's fine. I think we might as well get aim for some consistency.
And OB already does it. And if our OB already does it, I feel like all of our ghost stuff probably already does that, or it's very easy to make it.
**Antoine Toulme (Splunk Inc.)** 15:26 Yeah, it's the same people doing Go Contrave anyway, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:29 Yeah.
Yep.
**Antoine Toulme (Splunk Inc.)** 15:32 Okay.
Oh, that's cool, I mean, it's good progress, and we just need to kind of, Understand who is that contributor, why… Also, but that's a discussion that we can differ with.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:45 that.
Only other question I had on there is, kubernetes as a tool.
**Antoine Toulme (Splunk Inc.)** 15:56 Creates as a tool.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:58 Yeah.
There's like just, I haven't really looked into this, but they, Kubernetes made some kind of SBOM.
**Antoine Toulme (Splunk Inc.)** 16:06 Tool.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:07 I have no idea.
How useful that is.
But if it actually does something useful.
Seems like… Improving that thing rather than another one.
Ha ha.
**Antoine Toulme (Splunk Inc.)** 16:20 Oh.
And of course, it's going to use a different format.
It's using SPDX by default.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:34 Again, not a big deal.
I don't know that we necessarily need to use it, or if it's even useful.
But…
**Antoine Toulme (Splunk Inc.)** 16:41 I don't know.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:42 It's an example of what another CNCF project did.
**Antoine Toulme (Splunk Inc.)** 16:50 Okay.
We should probably not build on.
Should be something.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:57 I'll mention that this exists. I don't know if it's useful because Kubernetes is differently shaped from our project.
They're a gigantic pile of Go code.
Whereas there are like nine medium-sized piles of codes in different languages.
**Antoine Toulme (Splunk Inc.)** 17:15 Yeah.
I haven't used… I haven't looked at the communities in a while, as a… Yeah.
Anyway, cool.
Okay, Thanks, Ted, for looking into this.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:30 Yeah.
**Antoine Toulme (Splunk Inc.)** 17:32 Burden.
Denis, I reviewed your PR and approved it.
**Denys Sedchenko** 17:42 Thanks.
**Antoine Toulme (Splunk Inc.)** 17:44 I… saw that… Big Kitty has some feedback, that's fine.
Okay, so… I'm guessing he's gonna get back to you on that.
You want to talk about R2?
**Denys Sedchenko** 18:05 Yeah.
Basically… Maybe I… Share a screen for a bit, just to show you what actually happens.
**Antoine Toulme (Splunk Inc.)** 18:15 Yeah, of course. Please go ahead.
**Denys Sedchenko** 18:17 Okay.
So… If I go to OpenTelemetry…
**Antoine Toulme (Splunk Inc.)** 18:27 Yep.
**Denys Sedchenko** 18:27 And I'll try to enable R2.
I am behind the paywall.
But I cannot click this button because I'm not the owner.
**Antoine Toulme (Splunk Inc.)** 18:39 Yeah, so what was our follow-up on that? I brought this to Austin. He said, oh, no, I need to open another ticket. Is that what it was? It's been a week.
**Denys Sedchenko** 18:49 Yeah.
**Antoine Toulme (Splunk Inc.)** 18:49 And then it's like, oh, I need to open a ticket, opening a ticket takes time, and can you… can I put you on a ticket? No, I guess I'm gonna be it.
So.
**Denys Sedchenko** 18:59 Yeah, and we didn't even touch the question of domain and, like, how to attach the domain. Do we need a load balancer?
You know, so… Stuff right now is available on Copper. I am able to trigger builds manually on my machine.
It builds from a fork.
But in order to have, like.
Our own domain, there is still stuff that… We're missing R2 and the main question.
**Antoine Toulme (Splunk Inc.)** 19:38 Okay, so on the 8th, so last week.
We opened a ticket with Austin, specifically asking him to help, Click the button for us. I'll let you know when I hear something back.
**Denys Sedchenko** 19:51 Thank you.
**Antoine Toulme (Splunk Inc.)** 19:53 That's what he said.
**Denys Sedchenko** 19:53 And.
**Antoine Toulme (Splunk Inc.)** 19:54 A week ago.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:56 Hmm.
**Antoine Toulme (Splunk Inc.)** 19:57 Should we ping him back and say, hey, it's been a week, what's up?
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:01 You should poke him, because he's been on the road dealing with, like, some family stuff and things like that, so… It would be…
**Antoine Toulme (Splunk Inc.)** 20:09 the.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:10 It would be worth poking him, because he may have.
Stop paying attention to it.
**Antoine Toulme (Splunk Inc.)** 20:15 Yeah, I feel for the guy. I think he's just living a honeycomb at the same time, so I'm sure he's got a lot on his mind.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:22 Yeah, but he also, I think, was, like, literally on the road, like, at the end of last week.
So it's anyways, just I would say poking.
**Antoine Toulme (Splunk Inc.)** 20:32 Okay, gentle ping, any updates, send to the group.
Alright, Dennis, if he gets back to us today, it'd be great, but then, you know, we'll see.
**Denys Sedchenko** 20:41 Do you have any, like, you know… What could be the right person to also, like, should we also ping him regarding the main questions as well?
**Antoine Toulme (Splunk Inc.)** 20:49 Yes, yes.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:50 Yeah.
**Denys Sedchenko** 20:51 Because we also have a certificate limitation, you cannot just, like.
Right. Issue a certificate for a subdomain.
It's a complex problem.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:01 Do you have access to Netlify?
**Denys Sedchenko** 21:04 known.
**Antoine Toulme (Splunk Inc.)** 21:05 definitely.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:06 that's where this stuff needs to get done. So I feel like maybe the question to get asked is, like.
Getting packaging maintainers access to.
Net Netlify.
**Antoine Toulme (Splunk Inc.)** 21:19 Okay.
**Denys Sedchenko** 21:20 There's also problem with the certificate.
So, SSL certificate has, like, also the list of, like, authorities that can issue another certificate for subdomains.
Right now, Netlify and Google in that list, but that's all, and, like.
for the… probably Cloudflare also needs to be in that list, so we can, like.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:43 the.
**Denys Sedchenko** 21:44 It's just subdomain.
There as well.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:47 Right.
Right.
And so that part… I don't know if Netlify Access gives you that, but if it doesn't, that would be a thing for Austin to do with his admin.
But two pieces, because I do think… regardless of where that gets added, you still have to go into the DNS management in Netlify and set up.
The subdomain to… To redirect properly.
I'm guessing you have to set up some DNS there.
**Denys Sedchenko** 22:23 Yeah.
DNS and probably… probably load balancer, because if we used a different cloud, it would require load balancer.
**Ted Young (Raintank, Inc. – Grafana Labs)** 22:31 Yeah.
**Denys Sedchenko** 22:32 So it's the second part to investigate.
**Ted Young (Raintank, Inc. – Grafana Labs)** 22:36 I think that's just where we're doing all of our DNS management.
for open telemetry IO. So some chunk of this will have to happen.
**Antoine Toulme (Splunk Inc.)** 22:46 I mean, if we have some law… if we can be a bit more dependent by having existence in DeFi, I think that's a… Great outcome, because… We don't want to be in Austin and Traskare all the time. We just want to make sure we don't overstep.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:03 Yeah. I mean, these are things we don't do very often.
And it's somewhat reasonable to leave the keys gated to some of these things.
Of.
**Antoine Toulme (Splunk Inc.)** 23:14 So, maybe I should open a new ticket, right? I'll just.
Open a new ticket, access to Netlify in community.
Does that make sense?
**Denys Sedchenko** 23:26 Maybe we can request a temporary access, so, like, when we fix, finish our stuff, they can revoke the access. It's just, like, a temporary measure during the experimentation phase.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:37 Yeah.
Yeah, I would… I would just be explicit about what you need to change, right? Like, you need to get this subdomain set up, so you need to change these DNS settings. I would say even, like, list those out.
And then say, you know, you also need to get Cloudflare allow listed.
**Antoine Toulme (Splunk Inc.)** 23:59 Yes.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:00 For these kinds of community issues, like, the more specific you can get.
In the actual thing, the… Better chance they are of getting done quickly.
**Antoine Toulme (Splunk Inc.)** 24:10 request access to Netlify… Netlify, pre-assisted, between now and the end of… November… 26 to, to sit up… A certificate… to… Serve traffic… a subdomain.
linking to Not fair.
Certificate to serve traffic.
And now.
**Denys Sedchenko** 24:49 We need the CAA records.
**Antoine Toulme (Splunk Inc.)** 24:52 see.
**Denys Sedchenko** 24:52 or Cloudflare.
Probably as well.
**Antoine Toulme (Splunk Inc.)** 24:55 Oh, but the… so, using a CA record? No, no, NS?
I,
**Denys Sedchenko** 25:00 Okay, I will repeat again, probably you're confused.
**Antoine Toulme (Splunk Inc.)** 25:02 No, I am always confused, sir. Yes, go ahead.
**Denys Sedchenko** 25:04 Okay, we have a DNS level of the problem, and we also have an SSL level of the problem.
**Antoine Toulme (Splunk Inc.)** 25:13 Yes.
**Denys Sedchenko** 25:13 We point, we added, we add the subdomain DNS record and point it to the Cloudflare.
**Antoine Toulme (Splunk Inc.)** 25:22 Yes.
**Denys Sedchenko** 25:22 This is Dion Estler.
**Antoine Toulme (Splunk Inc.)** 25:24 Yes.
**Denys Sedchenko** 25:25 Netlify manages the wildcard domain for OpenTelemetry.io.
**Antoine Toulme (Splunk Inc.)** 25:32 Mmm.
**Denys Sedchenko** 25:33 But when you point the subdomain to Cloudflare, Cloudflare also would need to respond with the appropriate certificate.
Correct?
**Antoine Toulme (Splunk Inc.)** 25:43 Yes, I understood. Thank you.
**Denys Sedchenko** 25:45 But the problem is that Cloudflare can, like, if Cloudflare will try to issue their own certificate for a subdomain, it will not work, because Cloudflare is not, like… browser will reject it because Cloudflare is not in CAA list. This is the, basically, SSL problem as well.
Right now, Netlify and Google are in CAA list. They added Google for their own use case.
It's, I assume, for Google Workspaces, because they wanted the mail to work, and we also need to add Cloudflare there.
**Antoine Toulme (Splunk Inc.)** 26:24 Interesting.
Okay, so you won't see it, that's fine. Do you want… we also don't have the domain, in CloudFare at all, we just need the… for that, usually we use NS, right?
Or just a…
**Denys Sedchenko** 26:45 I will be honest, I never connected an outside domain to Cloudflare.
**Antoine Toulme (Splunk Inc.)** 26:49 Yeah, right, same for me.
**Denys Sedchenko** 26:51 This is something I would need to investigate.
Probably, like, okay, probably… Umm.
I'll probably… I'll probably use something like Cloudflare Workers, they also have, like, load balancers or something like that.
just to issue a correct SSL certificate.
We will need to figure… I will figure that out later, when I have an access and I can poke stuff and see what works.
**Antoine Toulme (Splunk Inc.)** 27:16 Alright, so please give access to… What is your… Oh, my God! Sorry.
I swear, I'm not doing this on purpose.
What I'm gonna do here is gonna go to the… Read me, Paige.
and copy… All the names of all the maintainers.
Yes.
I think you guys said yes.
I'll just remove your affiliations, so it doesn't look like… I'll just remove also Damiano, because he doesn't care.
Douglas is not showing up, so we got Antoine Denis Mikkeli.
Good.
Okay.
Okay.
And that's it for that, so I'll just put it in the notes. Here's the issue, it's open.
**Denys Sedchenko** 28:24 One small thing, I got a bit confused.
So Antoine, you approved the PR, and Mikaela said that he will push some patches.
Should I wait for him to push some patches into the PR, or is it better to merge the PR and then he can push some patches? I've got a bit confused.
**Antoine Toulme (Splunk Inc.)** 28:43 I am from a school of engineering which consists of making sure that perfect is something on the horizon, not in the PR.
I like to merge stuff that's not working, and patch it with multiple small PRs, rather than having gigantic PRs with a big outcome. That is definitely not the way Mikity works. Mikity likes it when everything on main is always great, and then there's a bit of a… You know, he's… he's gonna… he's gonna work in the PR more than anything else, and so it's pretty… so it's more like a cultural discussion, and just not… You know, you should go with what Mikael feels, and if you requested changes, unfortunately, that means you're supposed to wait.
**Denys Sedchenko** 29:32 Okay.
Okay.
**Antoine Toulme (Splunk Inc.)** 29:34 Now, if he doesn't act on it.
And, you know, we can at some point say, look, it's been 2 weeks, we haven't heard back, let's merge what we have. If he's got feedback, he can open a subsequent PR.
**Denys Sedchenko** 29:47 Okay, because so far I don't see any explicit review.
Issues is just a follow-up thing.
**Antoine Toulme (Splunk Inc.)** 29:53 He's just, he's at his offside, so he's not going.
You know? That's the thing, too, is like, But… If you're not blocked, we're good. If you're blocked, please let me know. We can… we can talk to Michele and say, hey, do you mind if we get that in so that Denis can continue to work on the stuff he's trying to achieve?
Make sense?
**Denys Sedchenko** 30:16 Yeah.
Like, until we don't have… I don't have access to Cloudflare, we can wait for now.
But no. When we're going to have a first release, because this should be done before the first release, because all of the hooks are there, or the workflow is there.
**Antoine Toulme (Splunk Inc.)** 30:31 If you ask me, we have, in a month.
KubeCon NA. I'm on it by then.
**Denys Sedchenko** 30:38 Oh.
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:39 Thanks.
**Antoine Toulme (Splunk Inc.)** 30:40 Does that make sense?
**Denys Sedchenko** 30:42 Yeah.
**Antoine Toulme (Splunk Inc.)** 30:43 It's arbitrary, and it's not helpful, but I don't… I want to… I don't want to say things that keep calling any, like, we got packages.
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:50 I would say, you know, respectfully, in terms of culture, because we're still in the early stages, right, like, right now.
You know, the number one thing is don't be blocked.
So if it's helpful to get this merged so that you can keep working on different features, Denny, I would say it's, like, helpful to just go ahead and merge it, you know.
There can be a longer discussion about what the right way to do things is.
But…
**Antoine Toulme (Splunk Inc.)** 31:18 Yeah, I come from a school of thought where it's never perfect, it's a bunch of hacks piled on each other. This is what code is. And you just iterate constantly on the code, and every single contribution you can make is better, and I like small PRs that make things better.
Now, I'm very sloppy. My code is, you know, gives a lot of people a lot of heartache, including Mikkeli. And I… Just what it is, I guess, you know? So…
**Ted Young (Raintank, Inc. – Grafana Labs)** 31:47 Yeah, I mean, I think, like, you can get into some nuance around the shape of the changes, right? If it's changes to shared code that lots of people are using, it's so annoying to try to keep that sequestered way on… a branch for some big, gigantic change, right? Like, you're up in each other's business all the time. It's better to have works in progress that are getting merged frequently. Otherwise, it's just kind of crazy making, trying to get anything merged.
But also, it's better to, like, not have the code be designed so that everyone's working that way. Ideally, you know, you can go work on your new feature without… Having a bunch of, like, constant conflicts with… What other people are writing?
So.
**Denys Sedchenko** 32:37 Somewhere in the middle.
**Ted Young (Raintank, Inc. – Grafana Labs)** 32:38 Right? It's like… I don't think there's one right or wrong way.
**Antoine Toulme (Splunk Inc.)** 32:44 I mean, when someone… I think also, like, it's a good feedback for Michaela, it's like, hey, if you'd like to do that, would you mind if… is this good enough to merge now, and then address later?
So, anyway, he's not here. By next week, I think he's gonna get back to you very soon, don't you worry. He's very active, he loves… he works on weekends. This man is crazy. Wow.
So, he's gonna get back to you soon. I think by next week, we'll be unblocked completely. The blocker to me is Mark Lotfleur, right? So…
**Ted Young (Raintank, Inc. – Grafana Labs)** 33:17 Yeah.
**Antoine Toulme (Splunk Inc.)** 33:18 I'm worried about that more than anything else.
**Ted Young (Raintank, Inc. – Grafana Labs)** 33:21 If you're not blocked on that, I wouldn't worry about this.
Otherwise, we just… his branch becomes Maine for now, until he comes back. I'll just work off of that.
**Antoine Toulme (Splunk Inc.)** 33:32 That's fine. Okay, I gotta run. We have to go to the injector. It's great seeing you folks.
Right.
**Denys Sedchenko** 33:38 See you guys.
