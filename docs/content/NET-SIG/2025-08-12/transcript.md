SIG: .NET SIG
Date: 2025-08-12
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/dvPohXdPuIKsI95WohYbO_GlpAsPLGitgV6mSNFrToozC5UsU2Dx3Ht_vuFPUnL2.D7Dtd2ixzggKmiQS
============================================================

## Zoom Recording Transcript

**Martin Costello** 01:10 And….
**Alan West** 01:11 Hey, you again.
**Martin Costello** 01:14 Sorry.
**Alan West** 01:16 Oh, no reason to apologize.
… So I'll just give it a minute.
Hey, Seymar.
**Harsimar Kaur (Simar)** 02:28 Hey!
**Alan West** 02:32 Remind me again, you're on Raja's team, right?
**Harsimar Kaur (Simar)** 02:35 I am.
**Alan West** 02:40 Is he still back? Maybe, I think, after this week, I think I heard?
**Harsimar Kaur (Simar)** 02:45 Yeah, this date that's listed is Friday, but I'm thinking it's probably gonna be Monday.
**Alan West** 02:51 Got it.
Well, it might be a real small group, might just be us.
… I guess there was just one… thing that I was kind of looking at.
That maybe we could talk about briefly.
… Martin, I know you had been… Spending a lot of time reviewing this PR, and… I was just starting to kind of, like, look at it the other day.
… It's interesting to me, I'd noted that there was a previous attempt to do something similar, one of these that he's linked here.
And I think… My memory serves me, on one of these.
the attempt was actually implemented, I think it was this guy?
Yeah.
… I've not given this, like, a very close review. It's a… it's a relatively big PR.
… Touches a lot of things.
But… just observations.
I noted that It seems like this guy's goal is… Maybe slightly different.
then… this guy.
I mean, I think there's overlap, but… … the current PR, My read is that he's mostly concerned about making things support, you know, WebAssembly or Blazor.
Whereas the other guy, I think that was also a concern of his, but really, he was… he was focused on this… this whole thing of, like, oh, you know, you're… you got these long-living… Background threads that are just sitting idle.
And that bugged him for whatever.
probably good reasons, but also, like, I guess my question was, like, how… how big of a concern, really, is that?
Yeah, he's, like, sitting idle 99% of the time, yeah. He's not… he's right about that.
… between those two concerns, the thing that I guess, interests me most is this, right? Like, this, this… supporting… Of platform that we don't… currently support.
few questions that I have is that, like, one, is this it? Like, basically.
If we just fix the batch export processor and… the metric reader.
Does that… does that actually bring us into supporting? … Blazor?
**Martin Costello** 06:02 I guess… like….
**Alan West** 06:05 Yeah.
**Martin Costello** 06:06 rightly, you know, like, putting your hand up and swearing an oath? Probably not.
But there is… I can't remember which repo, if it was this one or the other one, but there has recently been a PR from the .NET team.
to add support for Blazor metrics.
So, they must be doing some testing somewhere to validate their end is working, if they're then doing PRs here to change things. So, whilst that's not official, 100% ironclad guaranteed, yeah, we work in Blazor.
It sounds like somewhere people care about that scenario.
So maybe there's, like, a tangential question is, should we be testing it works with Blazor?
**Alan West** 06:52 Yeah, yeah, totally.
… Yeah, and I think we should, if… if that's… if that's really the, … the primary objective, which is, like I said, the more interesting objective, as far as I'm concerned, than the, ….
**Martin Costello** 07:12 It wouldn't surprise me if the Microsoft folks are testing it Through the lens of Aspire.
Whereas Jerome, I believe he maintains… the UNO platform.
So he's probably got a specific use case that's blocked, and that's where this PR's come from.
So we've probably got two groups of people trying to do subsets of hotel with Blazor.
and they're overlapping, fixing bits they care about. Yeah, we probably don't have an end-to-end, this all definitely works in Blazor, or this definitely doesn't, and we're telling you it doesn't, because it doesn't on purpose.
Kind of statement.
**Alan West** 07:56 Right, at least know the edges of what we do and don't, if that makes sense.
**Martin Costello** 08:02 I have a similar thing, for a library I maintain. It's like, every now and again, we get questions… I get, like, oh, this isn't working properly in Blazor, and I'm just like, didn't know it did.
**Alan West** 08:14 Huh.
Yeah, so I didn't, … I don't know, Jerome, it sounds like, yeah, is he… is he with Microsoft, or…?
**Martin Costello** 08:25 I think he works for the Uno platform, which is, like, its separate open source thing, because I think… I only know what it is, because… have you ever used the NuGet Package Explorer?
Like, if you go to NuGet.org, you can, like, click on a link and inspect the internals of packages.
And, whenever that boots up.
it says, like, powered by Uno platform.
**Alan West** 08:50 Oh, that's cool. Is it a… you said it's available via the web?
**Martin Costello** 08:54 Yeah, so if you just search for any package.
And then, on the right-hand side, see it open in NuGet Package Explorer?
**Alan West** 09:06 Oh, I think I have seen this before. Yeah, yeah, yeah, yeah, I've forgotten about this, though.
**Martin Costello** 09:11 So you see in the bottom left corner.
**Alan West** 09:14 Yeah, yeah, yeah, yeah, and I recognize the logo, too. I, I think I've used the desktop version of this. This looks… this interface looks very similar.
**Martin Costello** 09:24 Yeah, I've used both versions, like, this is, like, the quick one to use, but it doesn't support scenarios like inspecting all the information in the DLLs and, like, things like signing, so sometimes I have to use the desktop version. But that's how I know who you know are.
Because it runs this, and I assume this is all Blazor.
**Alan West** 09:46 Gotcha.
Cool.
There's a little… Fun fact.
… Yeah, so, coming back to this PR, … Even if this is only, you know, ultimately fixing Things for, you know, a specific, specific thing, and… That, that's still a… A positive step forward, in my opinion.
… I'm not… given that I haven't looked super closely at the PR yet, I don't have, like, a concrete thought, but I'm not… Super excited about the new… … API.
Or configuration option.
I guess the one question I had was, like, if this is mainly for supporting WebAssembly, I wonder if there's, like, if we can do a platform check or something.
That would automatically enable it.
….
**Martin Costello** 10:54 Hmm. Yeah, I hadn't thought of that.
That's a reasonable suggestion.
**Alan West** 11:00 It gets away from… and the reason why I bring up this original guy's PR is that it gets away from, I think, what his objective was.
Which was just… you didn't like these background threads, but… specifically for supporting this, like, I think, like, a platform check would mean no new public API, and we'd still, you know, get….
**Martin Costello** 11:25 Hmm.
**Alan West** 11:26 Get some benefit.
**Martin Costello** 11:28 Yeah, because I think, like, I had… to be fair, I didn't read the previous PR descriptions to grok the justifications.
The threads thing, is it mainly an implementation detail?
**Alan West** 11:44 Yeah.
**Martin Costello** 11:44 You might not like it, but that's just the way it's implemented. You can't go through every third-party dependency and tell them that you don't want them to use threads.
**Alan West** 11:56 Great.
**Martin Costello** 12:04 Yeah, maybe there's, though, separate to that, there's, like, an open question we sort of alluded to already, it's like.
is there some minimal test leg we can add somewhere that does, like, a bare minimum validation on Blazor? Because I'm sure this person, if this was merged, and it didn't work, he'd come back and fix it.
But we don't have anything to guarantee that we keep his scenario working.
Here, or in any of the libraries.
Other than code that is shared to all the implementations of the runtime.
**Alan West** 12:43 Yeah, agreed. That's a great point.
… I think… Yeah, I'm gonna leave.
After we're done talking here, I'm gonna leave, you know, just kind of a summary.
of some… Thoughts, even having not, you know, looked super closely at the implementation.
But yeah, I like that thought of, like, hey, you know.
This would be great to achieve.
some support for Blazor.
Be nice to have some tests, to your point.
And then I'll pose this question about, you know, can we… can we get away from… Exposing new public API, and maybe just make this a… Like a platform check or something.
Maybe he can comment on… The feasibility of… of those things.
in your review of this PR, did… did… is there anything else that kind of… Came to your mind?
**Martin Costello** 13:52 I think there was… there was a few… there was a few, like, detail specificities on what they'd done, and those have all been addressed. Yeah, I'm still… I'm still feeling my way to the sort of the… how does it fit holistically in air quotes sort of thing, whereas.
I'm a lot more comfortable just looking at the code as it is and going, this is a good way of reaching that goal or not.
**Alan West** 14:19 Yeah, understood.
Okay.
Cool.
… I think that's the main thing I want to discuss.
I know, Martin, you still have a few things out here that… Just been sitting on, but we'll… we'll get those moving soon.
Oh, there's this OTLP exporter thing I was hoping that, … I didn't really… I thought Raj was gonna be back more the end of… July, so this went a little bit longer than I… had originally thought it would, but, I was kind of hoping that he would re-engage with this… with this individual.
… Other than that… Inc.
As usual, I haven't really looked at… I don't know if there's anything in the Contrib repo that anybody feels.
needs attention. I know Peter's out, … Is there anything here that you think is worth looking at?
**Martin Costello** 15:23 And let's quickly load it up.
Oh, but yeah, there's one that I did make a comment on, but in deference to a bigger question to be asked.
Which was, someone's opened a PR to add an open search library?
But it's, you know, it's 1500 plus lines of code being added, and then they've just copy-pasted the owner as… the group, rather than a specific person, so I didn't read the code… I haven't reviewed the code, but I just sort of slightly hinted at Someone has to decide that we're actually going to pick this up and maintain it first, because you can't just throw a library at the repo and have it maintained forevermore.
**Alan West** 16:18 Oh, here it is, I see.
Open search support.
….
**Martin Costello** 16:24 Because it doesn't seem to… there's… it's from a first-time contributor, I'm not sure what their affiliation is, and there's no real justification for why, it's just appeared.
**Alan West** 16:36 Yeah, got it.
And it also doesn't look like they're… responding on the PR.
**Martin Costello** 16:49 That's true, I hadn't considered that, but yeah, I decided I wasn't going to spend my time reviewing the code if it was going to be something we didn't want to take on to support in the first place.
**Alan West** 17:01 Yeah, yeah.
Yeah, I definitely don't, especially since it's been 5 days since… whatever.
Some comments were made, and this person is not around. Yeah, I think it… yeah, the general comment about, like, adding, New libraries is that… There needs to be somebody that… somebody that is… a member of the OpenTelemetry community, That is willing to be… A maintainer, or whatever, a code owner.
of… of the package. … So given that this person is a first-time contributor, I'd guess that they are not A member of the community yet.
That's not a hard thing to achieve, but, you know, it does require them to….
**Martin Costello** 17:50 Yeah. I had a quick look at their profile just, and there's no organisations listed. It's not obvious where This has come from.
Because without getting into the politics of what open search is, you'd think it would maybe be an Amazon-sponsored thing?
And there doesn't appear to be any such affiliation.
**Alan West** 18:14 Hmm. Oh, is it an Amazon thing?
**Martin Costello** 18:16 I… and let… someone can correct me if I've misremembered, I believe it's the non… AFO GPL licensed version of Elasticsearch.
**Alan West** 18:28 Oh, interesting.
**Matthew Hensley / Grafana Labs** 18:30 That's correct.
**Alan West** 18:37 Oh, I see, and then whatever, Amazon has some… presumably has some support for it, but it's not necessarily an Amazon.
specific thing.
… Yeah.
Well, I can comment on this one too, just say basically what I just did.
Save, which was… whatever.
You know.
We can't accept this without… Code owner, you need to be a member of the OpenTelemetry group.
Link them over to the resources.
And the community repository.
For how to make that happen, and then, you know, on top of all that.
We still need to decide as a community. There needs to be some sort of a justification.
That this is something we want to maintain.
So, I can share that on here.
… Matt, since you're here, just… my eye just caught this. Oh, you've still got it in a draft, so… Maybe you're not ready to talk about it, but ….
**Matthew Hensley / Grafana Labs** 19:52 The… Diff is currently a mess because it builds on some things in an ASPNET targeting PR.
So, all it does… I took the, … The metric and trace handle stuff.
He added a SQL client, and I applied it to ASPNet when I separated metrics and tracing.
And then have gone the other direction here, and … We have a single client to use the shared implementation.
**Alan West** 20:25 Cool, okay.
… Right, right, right, okay, yeah, this is… Sounded familiar, I think you were talking about this in a previous week.
Cool. Okay.
… Well… Anybody have anything else?
**Julius Koval** 21:04 Yeah, hi, just a quick thing.
Oh, yeah. You mentioned, Raj. Do you know, when he's gonna come back, or if he's back, or…?
**Alan West** 21:14 Yeah, I think after this week.
….
**Julius Koval** 21:17 No.
**Alan West** 21:18 I, I don't know that for certain, but, Simar here is on Raj's… Team, and that's what, she said.
**Julius Koval** 21:28 Oh, God.
**Alan West** 21:30 I assume that that means that he'll be back next Tuesday, but, I mean… Until I… until I speak with them. I'm not.
100% certain of that, but….
**Julius Koval** 21:41 Okay, cool, thanks.
**Alan West** 21:46 Cool.
Alright, Joe.
See you next week.
**Martin Costello** 21:51 Bye.
**Julius Koval** 21:52 Bye.
