SIG: .NET SDK SIG
Date: 2026-09-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:34 Inc.
**Matthew Hensley** 00:37 Hello.
Not exactly a packed house today.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 00:57 No, Alan might join, because he messaged me on Slack just now, so…
**Matthew Hensley** 01:04 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:06 Am I remembering correctly that Raj said he was only going to come to these every other week now?
**Matthew Hensley** 01:11 I think that's correct.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:20 So that would mean… I wasn't here last week, but he was, so I guess that means he won't turn up.
**Matthew Hensley** 01:26 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:47 Give it one more minute, see if Alan shows up.
**Matthew Hensley** 01:52 Alrighty.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:53 Have you, have you got anything?
for agenda.
**Matthew Hensley** 01:59 I don't think so.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:23 I guess Komet can start, and then… If Alan joins himself… Oh! Speak of the devil.
**Matthew Hensley** 02:30 Hang on.
**Alan West** 02:32 Hey, how are ya?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:34 Good, thanks.
**Alan West** 02:35 I'm not the devil, what are you talking about?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:38 I was just, I was just saying, if Alan doesn't show up.
Well, Alan shows up, Alan shows up, let's start the meeting, and then you appeared.
**Alan West** 02:48 Sorry, I always, I always show up a few minutes late, because I've always got a meeting that's, like, directly prior to that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:54 That's on Tuesday.
**Alan West** 02:56 So… I don't mean to be that guy.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:03 But one day I'll learn to share Zoom, probably.
I always, I always shed more than I intend to.
There we go.
So, I've got… Sorry, what's that?
**Alan West** 03:37 Oh, sorry, I was just… Filling in the, agenda.
I was present last week, so I'm putting my name in two places.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:44 Right.
Yeah, so I've got a couple of things… on here, first thing was… is it time to do a new release? Because I think there's a couple of new APIs that have been merged recently, so that makes it a minor, not a patch.
And… I've… because I remember… I think it was the last meeting I attended, which was maybe 3 weeks ago now, Raj was asking.
whether we were getting near to merging the .NET 11 PR, which I think we should wait until RC2, Because, there's some changes for ASPNetCore that went in at the last minute, so it'd be good to test those first.
And also, it means that we're then not stuck not being able to do a new stable release without having to branch until November.
And it's been about a month since the last one.
**Alan West** 04:55 Yeah, that sounds good. What is your sense now of, like, How much time… You think we should give ourselves for, as… as the… as November is coming.
And a new version of .NET's gonna be released.
What's, like, your comfort zone?
In… essentially, we have a dark period, and like, how… how short can we make that without… You know, being uncomfortable.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:24 I'm probably a weird outlier, because I updated all my personal stuff to RC1 the day it came out.
But, I… I would… I would have thought the amount of users we have that will willingly and… Enthusiastically used the pre-release builds is probably a small subset.
So… if we wait… if we wait until, like, the final preview's released to then do our preview, then that gives us a month of change to accumulate that's unrelated to .NET 11.
But also means that we can more or less similar ship.
with the staple release, assuming nothing weird comes up through user feedback.
But I think… If you… Wait too long after the release.
I don't think we're gonna find… we're unlikely to find stuff that hasn't already been found, given it's… we've, like, tested every preview.
And also, Using my old company as, an example.
is, like, once the new version, major version of .NET releases, you start getting into the Thanksgiving, Black Friday, Christmas period, and companies institute change freezes.
Yeah. So even if they wanted to, like, test it out ahead of full adoption in production.
they don't have much time before, they'd have to delay that until January.
And then you end up with, like, you know, like, February as the time And then a whole quarter's gone by.
**Alan West** 07:08 Yeah.
So you're an advocate of getting, a release of the OpenTelemetry.net library out, like, as… almost as soon as the new version of .NET comes out.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:23 Yeah, particularly because, excluding diagnostic source, people are only going to use the new stuff if they're targeting the new version anyway.
**Alan West** 07:34 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:34 So, if they're… if they're keen, there's a stable version, they can just use it, and if there's a problem, it can be fixed. And if they're not super keen.
They're only using one part that's 11, which is… which would be stable anyway, and… I don't think there's anything that's come up in Diagnostic Source over the last months.
That's been directly related to… anything we do, and I think the only specific change that's in for 11 that we've built on top of is a new Enum member.
But the, W3C trace, the context level 2 stuff.
**Alan West** 08:21 Inc.
Yeah, that'll make sense.
Well, yeah, but with respect to the… the pushing… pushing a release now.
Seems reasonable. Remind me again what the new APIs, where it was all the trace state stuff?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:40 So… I mean, you mean, you mean separate from the 11 stuff?
**Alan West** 08:46 Yeah, yeah, yeah, what would go in 119, basically?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:48 There's the… there's the… there's the Always Record Sampler, which is new.
**Alan West** 08:55 But she's just… Oh, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:56 or trace sampler.
But, I happened to spot in the spec compliance matrix that we didn't implement.
But it went stable about 4 months ago. And there's a new… convenient API that Steve added.
Which… adds.opentelemetry on the web, builder.
Which I think… is… The primary motivation around Inc. was, like, as a building block towards all of the declarative config work.
**Alan West** 09:30 Right, right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:32 But it's just, like, suite… It's just sugar for making it easier to configure things. There's also… I think everything else is either performance optimizations.
Or small tweaks, and there's one bug fix that the .NET team wanted.
To fix Blazor.
**Alan West** 09:53 Oh, yeah, yeah, that's right, that hadn't gone out yet.
Cool, yeah. I mean, it sounds good to me.
With respect to the always record thing, I actually only learned about that just a few weeks ago myself, and I… seen… I'd seen that you'd done something about that.
Do you know anybody that's actually using that? That record-only span has always been kind of, like, dubious to me.
From the standpoint.
Like, why… why does anybody want this? What's the use case?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:29 I don't actually know, if I'm honest. There's, like, some… Something I've started to do in the last couple of months or so, is I started watching the issues in the spec… what was it the semantic I mentioned? One of the other repo. So, because in the last couple of months, we seem to have been, like, quite reactive.
Being like, oh, there's a new spec thing, we should probably implement that, rather than knowing things were coming.
But yeah, this was one that predated me starting to do that, so… I literally just found it in the, in the Matrix.
**Alan West** 11:07 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:09 But it seemed so… Self-contained and trivial, given it was stable.
It just seemed like an easy thing to just tick off the list and not have to think about.
**Alan West** 11:20 Yep. Agreed.
Yeah, I think…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:28 I think there's a bunch of… I did… I, I had another scan of the repo with Fable today, and it's dug out a few things.
So, I think there's a few PRs, and I think… I think you've got a couple open, Matt, as well.
So, maybe there's a few more things to accumulate, just to round things off, but yeah. It sounds like you can do a 1.19 soonish.
**Alan West** 11:58 Yeah, sounds good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:01 Next item is something Piotta… DM'd me weeks ago, and I said I'd do something, and then I forgot. And then he poked me about it again this morning. There's a PR open, in the… there's two Prometheus exporters, and… for a mix of historical precedence, and because it seemed to make sense, both exporters export an enum type with the exact same name, and one of the codec scans that Splunk have running internally on the SDK repo Flagged that if you wanted to use both at the same time, and the types… conflict, and it's a bit annoying. It would be annoying.
I think it's a bit of a weird edge case, but I've opened a PR that would fix it.
I just wondered what other people's opinion on it was.
**Alan West** 13:00 Interesting. Yeah, it definitely does seem like a bit of an edge case. I don't know why people would be taking a dependency on both of these exporters.
In a single codebase, but… That aside, I don't know, Prometheus ASP.NET Core Translation Strategy.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:24 Yeah, I think for me, it's like… I would almost just go, oh yeah, fine, let's just rename it to Show Up the AI. But to make it work, the name's horrible.
**Alan West** 13:39 Yeah Yeah, the name is… the name is not exciting, but, I mean, I don't know. The, the alternatives probably aren't exciting either. Like, what we could… Instead of in the name.
Instead of renaming Prometheus Translation Strategy, we could add another component to the namespace.
Which I think kind of goes against what we've done in other places, like something like OpenTelemetry.exporter.prometheus.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:07 Yeah.
**Alan West** 14:08 Or, like, ASP.NET Core Prometheus versus, like, blah blah blah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:12 Yeah, I said… I said to Pyotr in the DM, it's like, ideally, when these were created, they would have had more specific namespaces to begin with.
**Alan West** 14:20 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:21 So to, like, do it that way, you have to effectively rename every type.
I think that's even worse at this point.
**Alan West** 14:29 Yeah, yeah, yeah.
That's… And then I guess the other… the other option that would not probably be Would be more work than… Then would make sense would be to, like.
Pulls stuff into, like, a common… common library that is… Shared among the two.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:58 Yeah, I guess you could theoretically do that, but… All of the code that's shared at the moment is intentionally internal.
So, we don't have to.
**Alan West** 15:07 Oh, this isn't.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:08 the surface.
So, the previous option was, like, a shared type.
That was in the namespace, and then both publicly exported, but all of the rest of… most of the rest of the code that uses it is internal.
So if you, like, if you went down the shared code route, you could do that, but I think you'd end up with an assembly that just basically exposes one enum, as far as public code is concerned.
**Alan West** 15:38 Right, right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:40 With, like, internals visible too, because… for everything else, because… Had all the shared code been public?
the work I've been doing over the summer to stabilize things would have been a lot more difficult.
Because I would have to keep all of the binary compatibility.
**Alan West** 15:58 Hmm.
Hmm.
Anyways, I don't have… I don't have a strong opinion about this.
looks… The name's like… occurrence, but I don't think I really care.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:14 I think on that, unless you have a dissenting opinion, Matt, I think I'll just go along with, Pierce's suggestion, as he seems to be quite strongly against making the change.
And I'd rather not, but I'm not gonna die on the hill.
**Alan West** 16:34 Oh, he does… he does not want to make… oh, no, he's.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:36 No, sorry, he does, he does want to make change.
I think it's a bit unnecessary for a weird edge case just to make Codex happy.
But the only thing that makes me not want to do it is just the naming.
**Alan West** 16:51 Yeah, the naming is ugly.
And it's like, even if this… even if somebody ran into this edge case, like, they… they could work around it. It might be a little bit annoying, but… It's not impossible.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:09 Hmm.
**Alan West** 17:12 Or actually, how would they? No.
No, that would be a problem, huh?
If somehow they were taken to dependency because it's in the same exact namespace.
Is there… I'm forgetting, is there a way to, like… in a using statement inside of a code file, like, be… Clear about which assembly you're referring to?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:46 I know you can do stuff with Global, but I can't remember if you can assembly qualify as well.
Maybe it's just easier to take the chip than even think about it.
**Alan West** 18:04 Yeah.
Shipping, it seems fine.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:12 Yeah.
**Alan West** 18:13 I don't know, get… I mean, maybe, maybe, maybe Raj has an opinion, I don't know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:19 I'll leave it until tomorrow, and then if it's… if it's still there with no feedback from anyone else, I'll just merge it.
**Alan West** 18:25 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:27 Cause it… cause, yeah, it was like… I'm not pro the change, but in a low-key way. So if someone had, like, a really good reason to not do it, then I would have probably sided with them. But if there's no strong opinions other than Piotras to take the change, then we'll just take the change.
Especially as we've already done it now.
**Alan West** 18:54 Yeah.
Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:57 Well, so the only other thing that I had left that I'd specifically put on the agenda was… I… I did put a message in Slack about this last… I think it was last week.
I saw someone in a different project, I don't think it was even a hotel.
Was asking about authenticode.
And apparently, Linux Foundation has a setup excuse me, to… to Authenticode signing through Azure Artifact signing, which is something I've used before anyway, to do Authenticode signing, so we don't have to worry about provisioning or money, it's just paid for centrally.
The only disadvantage is all the binaries assigned as Linux Foundation, not OpenTelemetry, so there's potential confusion there.
But, because I knew we had an old issue where someone had asked for authenticode, which I closed off last year because we didn't have the way to actually do it.
And because we've got other mechanisms for provenance, like, the SIG store stuff.
And then it just so happened that yesterday, someone opened an issue. They said it was a bug, I've changed it to a feature. They're just like, they… for some reason, they've got their system configured in a way that it rejects running any of the hotel DLLs, because they're not authentic code signed, which I think is a them problem, not an us problem.
**Alan West** 20:22 Yeah. Yes, that's a them problem.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:25 But, it's another mark on the tally board of people who've asked about it. So, I was wondering what other people's opinions are of whether we should… Pursue trying to do it.
**Alan West** 20:41 I know this has come up in the past, and I believe that there's been some efforts. I don't… I don't know… What became of those efforts, really?
I was never super involved.
I don't… I don't think it's a bad thing. I mean, you know… If we had some cycles, or if you had some cycles to basically, like, try it out, sounds good to me.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:11 The… the… It's a difficult thing to try, because you have to get access to the certificate.
to use it. So, it would… you would basically have to go, LFX, can you set it up as if we're definitely going to do it?
And then we'd have to experiment with it from there to actually do it, and we're gonna have to change the release process slightly to do it, because we'll need to build everything, and then if it's, like, a proper release, although not for testing, for proper release, then you have to go and sign everything as a separate leg.
And then publish from there.
So the release process will need to change as well.
But, and also, if we do do it, I think in the short term, we wouldn't sign the packages.
Because… NuGet currently has a weird workflow if you sign packages with authentic code, that means you have to manually upload the… if you're using Azure Trusted Signing Places, you have to manually upload the public key to NuGet every time before you publish the packages, because… You get authentic code, you have to upload the public key.
Which kind of makes sense. It's like, you know, is this package signed with a key that we know you own?
But, because Azure Trusted Signing Inc. uses short-lived certificates, they only last for 3 days.
So, in practice, if we know we're shipping once a month.
it means you have to manually go into NuGet and register it.
Between it being signed, when you know what the key is, and uploading it.
Otherwise, all the uploads fail. So it just adds manual friction into the release process.
If we did… I've been watching the issue in GitHub, which is basically to make that problem go away for, like, over a year now.
But, because I think Microsoft.
**Alan West** 23:12 There is… there's some dream of it being more automated, but…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:16 Yeah, yeah, I think…
**Alan West** 23:17 Is it a Nougat side thing? Like, they have to do something?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:21 I think NuGet… I think what the issue says is something along the lines of.
either, can we have an API so we can upload the thumbprint, and if not, can you special case the Azure Trusted Signing Route Certificate.
In some way, that means we don't have to do this re… this re-upload dance all the time.
But they haven't implemented it, so, I think for our own sanity, we probably signed the binaries, but not the packages. Which adds an extra level of complexity, because the tooling that signs stuff If you give it a NuGet package, it will recurse into it, sign everything in it, and then sign the package for you.
But if you don't want to sign the package, it means you have to manually unpack it, sign it, and put the stuff back in.
**Alan West** 24:12 I see, so he… you don't get the advantage of the tooling. You have to do it all yourself.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:18 Yeah, it's, it's, it's, it's an annoyance, don't ask me how I know.
But, but yeah, I just figured I'd ask if people thought it was worth trying to go down the route of trying to do it. And then, if we can't do it for any reason, it's not the end of the world. But, if there was a reason not to do it, then not even bother trying to do it.
**Alan West** 24:47 I don't think there's a strong reason not to do it, just a matter of… Whether we want to go through the hoops now, or… At another time, and I guess… I guess my other question… I'm relatively ignorant in this area, so I… I don't know, but is it… is this at all… Applicable to other language ecosystems, or some flavor of this?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:12 So, it's applicable to anything that ships to Windows within a subset of certain file extensions. So, in theory, if anyone's shipping a .exe.
or a .msi, like an installer.
They could slash should also be authenticode signed, because it removes Windows friction.
I think Azure Artefacts training might work with JARS, but I don't… I have zero knowledge of how any authentication like that works for Java binaries.
Oh, and it also… it could be used by Zero Code for their PowerShell install scripts.
Because you can authenticate some PowerShell scripts as well.
So there's… there's definite utility outside of our two repos.
But the definitive utility I know beyond those two is one more.
But, yeah, I don't know which SDKs and distros might ship DLLs or EXEs.
**Alan West** 26:32 Good.
In the Slack thread, I just noted that Carlos, you know, asked about, like, worth being in the GC? I don't know, doesn't look like there's been any…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 26:43 Yeah, I was just sort of letting it… maybe accumulate someone, but no one's replied yet. So yeah, I'll, I'll follow up on the quote-unquote branding.
Aspect of it, whether that would cause any… pushback from the GC, and I'll poke my friendly, GC member I know about that, and… And then if there's no concerns there, then… we should be able… if I poke the right people at the next foundation to get the repo set up.
then, I can take it as far as, you know, as a one-off, allow, like, a specific branch for a specific PR to do signing.
And then set up the flow so that we've got a binary that is all signed, and then we can look at it and check we're happy with it, and then… Incorporate into the release process from there, if we're all happy.
**Alan West** 27:45 Sounds good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 27:51 And so I had… Specific gender items.
This dashboard has an update.
If it's… if it's still broke tutorial, poke trash.
Go, why hasn't this been updated?
**Alan West** 28:16 What's the… what's the cadence again? Alfred?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:19 It's supposed to be real time, as far as I know. What?
**Alan West** 28:22 Not really, just a… More or less real time.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:24 I think there's something running in… I forget the name of it. Compute on-demand service that listens to the webhooks. Netify, that's the one. There's something in Netflix… Netify, I suppose this is the webhooks. So, looks like something's got broken.
Because nothing's changed.
**Matthew Hensley** 28:42 I'm leaving comments on my PRs. Every time you open one.
When it processes the web poke, it lets you know that it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:49 Yeah, that's true.
But maybe the dashboard's just broken, then.
Let's do it the old-fashioned way.
Yeah, that was the… what were you just told me.
Oh, they opened that one.
It's these two… I don't know if anyone else knows any… historical context on this, but someone opened a issue Saying that… It wasn't adding the telemetry-specific paths?
onto the OTLP endpoints.
And I replied, yeah, it's documented that you need to do that.
And… but then they were like, but why? And I don't actually know why.
**Alan West** 29:54 yeah, there's some goofy… my memory is pretty fuzzy. I mean, the… We could go look at the spec and try to refresh our memories.
might… not answer the why, though. I'm forgetting maybe the historical context.
**Matthew Hensley** 30:20 I… think I might remember, but I'd have to double-check, but I think it matches the environment variable big behavior.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 30:34 Without thinking about it too much, that sounds like it makes sense.
Because, yeah, what I basically said to the person who opened this issue is, I don't know, and you don't know, and there's no value in me going and digging it all out just to write a comment that tells you what the answer is.
So if you really care, you go and look yourself.
**Alan West** 30:55 I mean, really the… Place to ask the question would be the spec repo.
I'm just forgetting exactly, like, the story. Matt might be onto something there, but I…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 31:13 Oh, yeah, yeah, that's cool. It was just if anyone knew off the top of their head what the answer was.
Because otherwise, yeah, it just seems a bit of a waste of everyone's time for us to go and do all the digging, because we don't know.
**Alan West** 31:25 Right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 31:26 Just to answer this question, whereas this person, if they really cared, they could pick it up themselves.
**Alan West** 31:33 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 31:35 If nothing… if we don't come up with anything in a week, I might have a quick look at the spec, like Matt said, see if that answers the question.
And then this one is… Proofta did reply to this and tagged Viraj, but he hasn't replied, is I noticed in… renovate recently, they've added a new feature where… let me open the… the dashboard.
Just to show… They've added a feature where if you're using dependencies that are, like, marked as, like, obsolete.
It'll tell you.
And I noticed… there's a… there's… the, X unit has been, like, explicit… explicitly marked as deprecated, and you should use X unit V3.
But XUnitv3 supports minimum TFM of 472.
So, even if… So, even when we drop 462, If we stayed on the X unit V3… I've lost the issue.
Sorry, if we stayed on not XUniv 2, then we would still need to continually use an old, out-of-date, no more patches test framework.
So… My suggestion was, for the test only, we'd stop having one-to-one parity.
and we move the tests up to 472 so that we can stay on a modern, patched, and updated test framework, even if that means it's not testing the exact same TFM that we compiled to.
And then the comment Piotr made was… about 470 in 471?
But there isn't currently a documented end of life for those.
So, either they're gonna suddenly go out of date anyway, as well.
Or they're gonna stay in support for, you know, Till the world ends.
So, assuming… 470 and 471, stay in support.
What are people's thoughts on… having the test versus TFM mismatch for .NET Framework.
**Alan West** 34:15 Well, specifically on this, like, 470-471 comment, like, correct me if I'm wrong, but I don't… we don't ship, like, a 470-471 of our…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 34:26 We don't today, but because 462 goes out of support in January.
**Alan West** 34:32 Right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 34:33 There's an implied raising it up to 470.
**Alan West** 34:38 Yeah, okay, okay, so that's the move you think we'd make.
Yeah. We just bump it up to the… Early.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 34:46 Still support.
Yes. So then that would… that would move the… all the stuff in source, up to 4.7.
But we would have to stay on the obsolete version of XUnit to also target 4-7 in the tests.
But if we went up to 472, we could then upgrade to Action UP3.
And then whatever new benefits that has. But it does create a gap between what we target in the test and what we target for the NUCA packages.
**Alan West** 35:21 I would venture to guess that the risk is low, but I'm not… There may be things that I don't know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 35:28 Because, yeah, something I did put in… here, it's in this paragraph, but the TLDR is… all the agents in CI have 481 installed on them.
So that they are using the latest possible version of Kotlin Framework, they're just running it in the compatibility mode that makes it behave like… 462.
**Alan West** 35:51 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 35:52 So… If there is a gap in how it behaves.
Then, it's, yeah, it's probably a very small surface area.
a behavioral difference.
Especially because we're not doing anything, like, you know, testing stuff in, like, real IIS.
**Alan West** 36:14 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 36:17 I just remember that at some point in the past, when I suggested we upgrade to XUnitv3, I think it was Piotto, but someone said, oh no, but we need to test the same version we ship, so that's why we're not using V3, because we can't use it.
But with the end of support in January forcing us to move up.
I figured it'd be a good time to revisit that decision.
Considering that old XUnit is now out of support as well.
**Alan West** 36:58 Yeah, again, I think that sounds reasonable. I… I wouldn't be… I don't have a reason to be all that concerned, but if somebody, I guess, were to point to a reason.
That there's, like, some… some risk that we don't know about, then, I guess?
There'd be something to discuss, but I just… I doubt that there's gonna be an issue.
I mean, especially even as you point out, like, you know, the test, like, CI is running 481, and running in some compatibility mode. I mean, there might even be a risk in that. Like, you know, it's not true 462.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 37:37 Hmm.
**Alan West** 37:45 the kinds of issues that would surface from this would be, I think, pretty esoteric, and require, like, a very specific environment.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 37:55 Hmm.
**Alan West** 37:56 I don't know, does that make sense?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 37:59 Yeah, that makes sense to me. Were you gonna say something, Matt?
**Matthew Hensley** 38:02 Yeah, I think because .NET framework and friends are a server component now, they're not even shipped separately.
That I… don't know that you can even actually install on a supported version of Windows Server an older runtime. I think it… I mean, they're supported Right? Like, they're not end of life, but… Might even check, because the modern installs might not even be able to run anything but 481 in compatibility mode.
**Alan West** 38:36 Yeah, and I mean, I wouldn't even… I wouldn't even suggest trying. Like, I think that that would be… going through, like, ridiculous hoops. I'm just, you know, commenting on, like, yeah, you know… there's somebody probably still running stuff on some old version of Windows Server.
Out there that actually can… run 462 and… Or, I guess in this case, 4-7, right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 39:06 Hmm.
**Alan West** 39:07 And maybe our tests… Because our CI just doesn't run that old-ass version of Windows servers, maybe our test could… miss something, I don't know.
Seems pretty unlikely.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 39:20 I think if we would… were to get grief from people, it would… the more likely vector is, you don't support 462 anymore, but we're still using it. To which our answer would just be, yeah, but it's out of support now.
That's your problem, not our problem.
**Alan West** 39:39 Yep, I think, Yep, I agree. That's gonna be the harder thing for people.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 39:52 What I might do on this issue, then, is… when I've got some… Because it's probably going to take a couple of hours to do. I might spin up a branch to do the migration work.
And see what falls out of that, because I think if we are willing to go down this route, I think it makes sense to do it sooner rather than later, and have to leave it to do… update the test and all the TFMs in January.
**Alan West** 40:20 Huh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 40:21 We can just get it out of the way.
Especially as I doubt we're going to make any substantive changes that would affect all their framework in the next… Four months.
**Alan West** 40:38 Yeah, that sounds good. Just one more comment about the 462 people that are gonna be, you know… I think they'll be able to… they'll still be able to use new versions, because we still ship a net standard.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 40:49 Yes.
**Alan West** 40:50 Version of things, so…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 40:52 They might just have… if I remember correctly, 472 is the version that made net standards not be stupid.
So they might still have binding redirect.
fun, but… That's probably not new anyway.
If you're on a version on the level 11.2.
**Alan West** 41:17 Cool, yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 41:19 Are there any interesting PRs open right now?
I don't think there's anything beyond… Ones that are just waiting for people to, like, take a look at.
Contrip… There was a… I… I think… leave this one for Raj to take a look at in the first instance, but someone from the .NET team Logged an issue yesterday to do with how the disk persistent storage stuff works.
I think they've made some changes for the .NET SDK in 11.
That uses it, and it doesn't work in some… or it doesn't work nicely in, like, short-lived apps.
For some reason… This one, this is on mute. I think you commented on this one, Matt?
Yeah.
So, someone's suggested exposing a very large amount of metrics out of the native half the library.
**Matthew Hensley** 42:41 I'm gonna look at their proposal, I think they put together a proof of concept.
Make sure it's scoped down to the minimal useful set.
Messaging SIG's not gonna get started anytime soon, and… I think Java's just shipping… Some de facto standard at this point, so might as well… Do it ourselves.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 43:08 Yeah, I don't really know much about Kafka.
Other than it, it does message.
**Alan West** 43:16 Do… actually, do we… we have Kafka instrumentation in the contribute?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 43:21 Yeah.
**Alan West** 43:23 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 43:26 It'd been there a while.
But I think it was, unloved for quite some time.
**Alan West** 43:32 Okay, and so then the native library emits metrics, but…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 43:37 So…
**Alan West** 43:38 like, fit the shape of the… of the messaging conventions, so, like, the Kafka instrumentation, the contrib…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 43:44 So, if I remember correctly, it's… not native as in it does it itself, it's, like, native as in all the Kafka SDKs build on top of, like, some C DLLs.
And then the library exposes an ability to breach in and get them. So they're not even meters.
If I understood correctly.
**Matthew Hensley** 44:06 That's correct.
**Alan West** 44:10 Gotcha, so they're, like, Probably pre-aggregated values that'll need To somehow be shimmed into… meters.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 44:29 I guess.
**Matthew Hensley** 44:30 Yeah, it's something like that. I need to go look and see, but… figure it's slightly possible since Java's already done it.
**Alan West** 44:37 Yeah, anyways. Yeah, curious, that probably requires a little bit of investigation, because… That's… a challenge that I think the community has run up against is Like, metrics generated effectively.
by a different API or different system.
How do we bridge them into the OpenTelemetry ecosystem?
and there's… I recall, I don't know… it might be stable now, but there was a metric producer API that we never implemented that's in the specification.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 45:20 For this purpose, there's… I recently read this issue, in the last 2-3 weeks.
There is an issue open about it, and so… and… I did a little bit of investigation and proposed an API surface to do it. What was it called again, Alan? I'll see if I can find it.
**Alan West** 45:40 I think the metric producer, API.
It's nothing I'd ever studied super closely, but… Just basically the premise of bridging metrics from a different system into OpenTelemetry. That's… that's the gist of it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 45:58 Yes, yes, so someone looked at this last year and got stuck.
Then someone suggested picking it up.
And I didn't like their suggestion, so I went and had a bit of a further dig.
And yeah, came out with this, like.
here's what we might want to do, but the main sticking point, from what I looked at, is because we would need to return metric I think it's metric.
Let me check.
Yeah, because we need to return a batch of metric points.
Metric point is like a struct.
But all of the constructor is internal.
And there's maybe a little bit too much implementation in the struct.
To populate the values.
So, if you, if you made it public today.
without adding loads of new APIs, there isn't a really good way to be able to actually hydrate values.
So, we're sort of, like, missing… A piece on how to… how someone could actually go, given all this information, make me a metric point.
**Alan West** 47:20 Gotcha, yeah, yeah, yeah. This is beginning to kind of refresh my memory. I hadn't seen this issue before, but yeah, like, that's what we would need to do, the metro producer, basically, the output, and it would need to be metric points.
Some translation to metric points.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 47:37 Yeah, because I think I've reached the point where it's like… It's internal, and there's loads of weird stuff in it for public use, so maybe we can make a factory method or something.
And hide it all away with a… dedicated different public API, which is, how do you give us the values for us to make a metric point for you? But that needs more thought.
**Alan West** 48:02 Sure, sure, sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 48:04 So maybe the Kafka thing will make this come up again.
**Alan West** 48:11 Yeah, I would suspect so. Again, yeah, if it's one of these… if it's one of these scenarios where it's, like, a metrics from another… of a different shape from a different system.
What was the context of this one, do you… do you know?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 48:24 I think this is just that David Ashpole.
**Alan West** 48:29 Oh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 48:29 Create an issue to track us implementing it from the spec.
**Alan West** 48:34 He's just saying, it's stable in the spec now, and he just opened it up in all the SDKs.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 48:39 Yeah, and then… and then it… and then I think it just sat there for ages. I slapped Help Wanted on it.
They didn't read it, it was just like, oh, it's summit stable, someone can do it.
And then I think two different people have looked into doing it and got stuck on the same… Bing we just discussed.
**Alan West** 48:55 Yeah, okay, okay, I see.
Well, interesting. So, anyways, we might have a concrete Scenario now, that…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 49:03 Hmm.
**Alan West** 49:05 With the Kafka, so that's cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 49:08 I'll quickly pick out Wes.
Matt, I've sent you the link to it.
In case it's useful to you when you look at the Kafka stuff.
**Matthew Hensley** 49:24 Thank you, and I replied to the, issue about why you have to pin the paths.
It was indeed.
Because that's how the environment variables work.
We're gonna set up your endpoints.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 49:37 Okay, cool, thanks.
And then… this issue got popped last week. Someone was basically going, why do I have to do… manually register all my meters and sources? Can't I do it from config? Can you build something to do that?
which then rang a bell with me. There is something built into .NET to do it.
In Extensions Diagnostics, which basically got a binding from configuration into something. I forget what it's called, but we don't… consume or integrate with the API at Hydrates.
So… It doesn't answer the question.
It's not like a magic, I'll just use this thing instead.
But, it might be something worth us looking into in the future.
Because then the… because where's the… because I had to quit going at this, because I thought, oh, I'm… use this thing. The idea would be that you just do add metrics, add tracing, and give it your config.
And so you don't have to do this.
anymore.
And then you just configure what you want in the app settings.
But there's a missing integration point between what this is configuring and what… how the SDK Listens to stuff.
So, we'd have to build… I don't think it'd necessarily have to be public API service.
It could just be internal glue.
But, I don't think it's a quick win.
So, it might be an interesting thing to maybe go back in the hosting integration at some point.
**Alan West** 51:38 Gotcha. You can do this via, No, we don't have a way to control this.
with… environment variables today, do we? Or maybe the… maybe the auto-instrumentation SIG has a way to do this, right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 51:57 is…
**Matthew Hensley** 51:59 Zero-code stuff can… subscribed activity sources and meters via… in VARs.
**Alan West** 52:06 Yeah.
But yeah, the SDK itself doesn't,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 52:16 Maybe, say, a 2027 side project to get that lit up.
Are there any interesting PRs that aren't just need to review?
Oops.
Yeah, I think… I think these are all just in the… in the set of need to review.
This one, Steve Tacoop.
Let's time reset this.
Maybe it's Raja. I'm sure BrightHa was very content on this, but I see it. Anyway, someone suggested… making pre-DOTNET 10 behave the same for instrumentation HTTP.
But… Oh yeah, it was Steve.
And, is just sort of, like, artificially making older versions behave the same way as .NET? Like, do we actually want to do that?
And… I'm kind of… In the same camp, which is like, well, if you want it to behave that way, upgrade.
Especially with 8 and 9 going out of support in… Two months.
And then we've got plenty of existing… precedent for .NET Framework behaving differently.
**Alan West** 53:47 Yeah, I don't think it's worth it.
Gonna drop those.
We're gonna drop those targets when the 8 and 9 go out of support.
And then… This user that's using some pretend target is gonna fall back to our… if they upgrade OpenTelemetry.
They're gonna fall back to our net standard.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 54:09 Stop.
**Alan West** 54:10 Again, and that's not gonna have the support they want, right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 54:15 Yeah, plus also… Is the HTTP instrumentation for Modern.net, and we delegate most of it to the runtime anyway?
**Alan West** 54:25 Right, right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 54:30 Yeah, I might have taken a bit of fitness tomorrow.
Bam.
Yeah, it sounds like it's… it's not an obvious… thing to add.
**Alan West** 54:46 Yeah, I don't think so.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 54:49 Yeah, that was… that was all the recent PRs and issues. Is there anything anyone else wanted to discuss in the last… Four and a half minutes?
**Alan West** 55:01 Nope.
**Matthew Hensley** 55:06 All good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 55:09 Oof.
Okay, so I'm gonna speak to you next week.
**Alan West** 55:15 Sounds good. Talk to you later.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 55:16 Bye.
**Alan West** 55:18 Alright.
