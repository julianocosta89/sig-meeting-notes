SIG: Networking SIG
Date: 2026-08-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Antonio Martinez (Cisco Systems, Inc.)** 01:46 Hey, everyone.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:51 Okay.
**Giuseppe Ognibene (Coralogix)** 01:53 Everyone.
**Sven Cowart (ElastiFlow Inc)** 02:04 Morning, everyone.
Or afternoon, I suppose, depending on where you are.
**Antonio Martinez (Cisco Systems, Inc.)** 02:10 Spain, yeah.
**Sven Cowart (ElastiFlow Inc)** 02:16 Somebody say something?
Hello?
**Antonio Martinez (Cisco Systems, Inc.)** 02:23 Could you hear us.
**Sven Cowart (ElastiFlow Inc)** 02:29 Let's try this.
**Antonio Martinez (Cisco Systems, Inc.)** 02:31 We're hearing you properly.
**Sven Cowart (ElastiFlow Inc)** 02:33 Okay, I couldn't hear you guys, I don't know why. Man, the speakers aren't leaking.
Right, let's get started.
I will share my screen.
Cool.
Just real quick, wanted to highlight this. We'll go to that agenda item next, but, if you guys… didn't see… Just announcing here that the, the project board is up.
So that's true.
This is here, I still need to create a roadmap with all this Loaded up, but you should have access to that. If you don't, let me know, because then I did something wrong.
And, but should be good to go.
And what I did to pull these in, I just took All issues that had… In their labels.
Inside of either the cement.
I think the semantic conventions, Rego, is the only one I focus on, but had the area of network And… Or our different areas, source, destination, and DNS.
So that's how we got… I got all those in, and now I've set up a, there's a workflow that… will auto-add something if it's in the semantic conventions repo, and it's an issue or PR, and it has the label source, destination, DNS, or network on it.
So anytime anyone adds that, they'll automatically get added to this board.
My next steps on this are to… Go through this, figure out what's the actual status for all these things, and then, follow that up this week with Trying to actually get some of these to… be in review, or have some type of PR related with them. I know, Antonio, you were already working on some of those things, so we'll just be collaborating on that stuff.
And then, and as I go through, my main goal still is to do a review of the existing semantic conventions to… to see where there's overlap and where we need to adjust things so that we can move forward with a little bit better of a foundation.
And then lastly, I need to create the roadmap, because that's a requirement for us, which I haven't done yet.
But once… next week, once I'm ready with the roadmap and determining the status of all these, I think we'll just have this meeting. I'm gonna start with a little check-in on this board, and then… Go to the agenda items.
Does that sound good?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:56 Thanks for setting this up. It's great.
**Sven Cowart (ElastiFlow Inc)** 06:00 Actually, probably makes sense to throw this up here.
Cool.
Who added… Source, destination, network, source… Yes, I'm guessing that was you, Antonio.
You're muted.
**Antonio Martinez (Cisco Systems, Inc.)** 06:28 Sure, by the way, I was mentioning, like, the… the bar looks really good before. For that one, source and destination, here is more like a follow-up about that ticket, that, we weren't… Having doubts if we want to have, like, network.source, network.destination, or… I started using source and destination namespace.
**Sven Cowart (ElastiFlow Inc)** 06:50 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 06:50 Because there were also some inconsistencies there, and different opinion, yeah.
**Sven Cowart (ElastiFlow Inc)** 06:56 Did you… did you join the semantic mention call?
**Antonio Martinez (Cisco Systems, Inc.)** 06:59 No, I think you were there, and you…
**Sven Cowart (ElastiFlow Inc)** 07:01 Should I know.
But, so I'll just kind of summarize what we discussed there.
I brought this up, we do think it's a bad idea to create a new source and destination and just reuse the existing one, unless there is a… I don't see why we would want a new one in this particular case.
Furthermore, on this point, I think, There was even a question if we need local and peer.
And the ask was that we need to look at the… Oh, boy.
Let's get up that.
**Antonio Martinez (Cisco Systems, Inc.)** 07:44 You can hear from me. Same problem.
**Sven Cowart (ElastiFlow Inc)** 07:48 Classic, as of late. Okay.
Well, because I can't open the hat, that's… well, but, I think that was about… The details were that There is also some confusion if we should just use local peer instead of networked outsourcing network.
destination, and the next step there was that we look at some of the SDKs and instrumentation libraries.
To figure out how is network.local and network.peer being used.
And, Farras specifically asked to look at the Java one, because he knows that they use it there.
And does it at that point.
make, does it make sense to just… Change those to source and destination.
or to, or come up with a reason as to why they should still be around. But more or less is… yeah, because we need to find a justification as to why Local and peer.
still exist.
And are being used, and the way we need to do that is to go through the code in various repositories to find Like the JavaScript, or Java one, where they're… he knows they're using it.
And figure out why, and if it could make sense to just use source and destination.
**Antonio Martinez (Cisco Systems, Inc.)** 09:16 I see, okay, that's clear. So, the idea, if I understand correctly, like, if we don't find out any blocker, why we need network.p or network.local, we can move it to the source. Destination.whatever, right?
**Sven Cowart (ElastiFlow Inc)** 09:32 Yes.
**Antonio Martinez (Cisco Systems, Inc.)** 09:32 Okay.
**Sven Cowart (ElastiFlow Inc)** 09:34 I agree.
**Antonio Martinez (Cisco Systems, Inc.)** 09:34 in the Jira, in the GitHub as well.
As I'm afraid of that.
**Sven Cowart (ElastiFlow Inc)** 09:41 Nope.
**Antonio Martinez (Cisco Systems, Inc.)** 09:43 Okay. And then, because the reason why, for me, that ticket is important is because everything that we do after will follow the same pattern, like the… like, the one that we discussed it about address AP before, address AP6, or ESN number, or prefix, all of those. If we continue with network.
local and peer, we will add it there. If not, it will be under source.address, or… Yep.
Okay, thank you.
So I will try to give priority to… to that investigation, and then we can… And that conclusion will need to be agreed, or… on the semantic conventional meeting, right? Not here, because we don't have in their privileges to duplicate those, right? We will need their approval.
**Sven Cowart (ElastiFlow Inc)** 10:30 But let's figure it out here and put our best proposal for it, and then we can sync with the semantic conventions, SIG to… to finalize it.
But yeah, I mean, just like this one, I think there's a lot of overlap and confusion about how to use some of those network attributes, and that's what… we need to resolve that and create the proper foundation, and so that's my goal as well. Across all of them, we need that right foundation to move forward.
Hey, Braydon, welcome back. Sorry during that.
**Braydon Kains (he/him)** 11:05 Yeah, sorry, I've been out for a while.
Great progress, glad the project board is up.
**Sven Cowart (ElastiFlow Inc)** 11:16 Okay, if we have nothing else, then…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:20 Sven, did you catch up with Rob about the UN64?
Creating an issue. The board would be a great place to, to track it now.
**Sven Cowart (ElastiFlow Inc)** 11:31 Yep, yep, so he's… he's gonna do that.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:34 Thank you.
**Sven Cowart (ElastiFlow Inc)** 11:35 bogged down with quite a few other things right now, so he hasn't made any progress on it, but yeah, I caught up with him and let him know our conversation exactly, and that he should create a, An issue within the specification repo, so…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:51 Okay, so will… will the board pick it up if it's created on the spec repo, as opposed… as opposed to the conventions repo?
Or do we need to add it manually, maybe?
**Braydon Kains (he/him)** 12:02 I manually add it, yeah.
**Sven Cowart (ElastiFlow Inc)** 12:06 I just need to change it.
One thing that's weird is I keep… Maybe I just don't know how… wait, why does this work? Oh.
No, I'm not gonna reload it. Where here… Can I add a new one?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 12:24 It… it might not… Let me… -Oh.
Yeah, I don't know, because the… is the project tied to the repo? This project looks like it's org-level, right? So I don't know if it is tied to a single repo.
**Braydon Kains (he/him)** 12:37 The projects are all org level, so you can… you can add from… from other repos manually. I think you need… the way I always do it, there might be a way to do it from this view, but I always go to the issue, and on the right side, there's, like, a little project drop-down, and you can at it that way. That's the way I always do it.
**Sven Cowart (ElastiFlow Inc)** 12:56 Okay, that makes sense. I, I had this one in… Maybe I can duplicate it, but unfortunately I can't pick multiple repos when I edit this.
But I'll see if I can get it to auto-add.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 13:13 Yeah, no, that's great, and as long as it gets added to the board somehow.
Then we've… we've got something to, to discuss next time.
**Sven Cowart (ElastiFlow Inc)** 13:22 Cool.
Alright, and I'll also… ping Robin about the entities, because we need an extra draft of that to move that forward.
Alright, that's it.
Take care, short one today.
Good to see you, everyone.
**Antonio Martinez (Cisco Systems, Inc.)** 13:45 Hmm, it's…
**Sven Cowart (ElastiFlow Inc)** 13:46 Bye.
**Braydon Kains (he/him)** 13:47 Thanks, everyone.
**Antonio Martinez (Cisco Systems, Inc.)** 13:47 zip.
