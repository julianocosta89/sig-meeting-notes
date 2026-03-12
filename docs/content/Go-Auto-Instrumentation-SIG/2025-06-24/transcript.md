SIG: Go Auto-Instrumentation SIG
Date: 2025-06-24
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/Yjw-vceQFCfEofG7TBwuqK3-pMKPS3LIBMzSTML07Luay_7nSvGjAMSa1KgXBUM.UkDQA6K_uGjHX4Fc
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 00:21 Hey, Tyler.
**Tyler** 00:23 Hey, Raphael, how's it going.
**Rafael Roquetto** 00:25 Good! Good! How are you?
**Tyler** 00:26 Doing? Well, yeah, just what's that.
**Rafael Roquetto** 00:31 How was your weekend.
**Tyler** 00:32 Oh, it's great. Yeah, it actually got some projects around the house done on Saturday, when it was like raining, which which is great. And then Sunday kind of cleared up and went for a little bit of a hike. And yeah, got outside. And so yeah, I mean, it's funny how like I really like the variable weather, I think the most so, having 2 months of sun is great. I love it, but I also like having rain once in a while. So, yeah, yeah.
**Rafael Roquetto** 01:00 I can relate, like we had rain here, too, on Friday and Saturday in. It's been mostly sunny, and then I would pretty much take that over rain if I had to pick one. But having some rain sleeping, you know, feeling that feeling. Yeah, yeah, I know what you mean. I was happy, too.
**Tyler** 01:16 Yeah, I do a lot of gardening as well. So it's nice to just like not have to be able to turn off the irrigation systems and things. And so, yeah, it's a lot of fun. And out here in Oregon, like like, it's kind of out there as well like the fire seasons are definitely in full swing. So getting some relief on the active fires is great, you know, to obviously for places that are impacted. But also like we got smoke in the, you know, the sunset and stuff. So yeah, it's nice.
Yeah, clear up a little bit. Yeah.
**Rafael Roquetto** 01:44 The important question is, did you automate your irrigation system?
**Tyler** 01:49 I mean, not really like I mean, yes and no, like I bought like a rainbird like timer, so technically is automated and like in in that sense, like, yeah, like, it turns on every day at 7, and like it has a.
**Rafael Roquetto** 02:02 Not a raspberry pi and custom stuff.
**Tyler** 02:06 No.
**Rafael Roquetto** 02:06 Okay.
**Tyler** 02:06 I mean, I I have. I have a raspberry pi that I thought about doing something like that, especially like getting like one of those like remote weather stations as well, because then, like, that's the feedback. That's the hard part, right? Is like getting some sort of like automated to know that like, hey? Like there's been.
you know, a quarter inch of rain. You really don't need anything, or, Hey, there's only been like a dusting of rain like, keep going or something. So it's like, Yeah, that'd be really great.
and then, like, then you can go buck wild, because then you could also like track nitrogen content. And you could start to like, do fertilizer or some sort of like injection stuff. And yeah, but no.
yeah.
**Rafael Roquetto** 02:41 Yeah.
**Tyler** 02:42 Yeah. Are you a gardener as well?
**Rafael Roquetto** 02:44 No, no! My garden is really sad.
I'm happy.
I live in that house complex. I'm happy. They they come and mow my, my lawn. I don't have to do anything. So yeah.
**Tyler** 03:00 Yeah, yeah, I I kind of get a lot of I don't know comments that like I don't. I grow. I think probably more flowers than I do like vegetables and fruit and stuff.
Because just about like I've come to realize like after doing this for years, like being in the garden is is more what I get out of it, and like food like it's always going to be cheaper if you go to the supermarket like.
**Rafael Roquetto** 03:25 Yeah.
**Tyler** 03:25 So it's always like, I just like, I just like, you know, building a nice like place to actually be and hang out. And so yeah, it's a lot of fun.
**Rafael Roquetto** 03:33 Yeah, I know what you mean. Yeah, for me.
**Tyler** 03:35 Yeah.
**Rafael Roquetto** 03:36 For me. That's being the driveway and washing the car. But just to be outside.
**Tyler** 03:39 Yeah.
**Rafael Roquetto** 03:40 In the 10 stuff.
**Tyler** 03:41 Or like go to a park, or something, too, is also great. Or yeah, like, exactly like just being outside sometimes is just great to to build a place that you can go do. That is great. So yeah, yeah, know.
**Rafael Roquetto** 03:54 Apologize. He can't come. Is his daughter valuation from.
**Tyler** 03:59 Oh!
**Rafael Roquetto** 03:59 School or something.
**Tyler** 04:01 Oh, yeah.
**Rafael Roquetto** 04:01 He's going to the ceremony. So yeah, he's not coming. So he asked me to.
**Tyler** 04:07 5 min in. I didn't have too much to talk about. Actually, I only wanted to kind of check in on our milestone.
which.
**Rafael Roquetto** 04:16 I'm not too much involved, so.
**Tyler** 04:18 Yeah.
**Rafael Roquetto** 04:19 Panel.
**Tyler** 04:21 I don't mean to. Yeah. No offense is meant. No, but no, no offense.
**Rafael Roquetto** 04:24 At all. I mean, yeah.
**Tyler** 04:27 No, I mean, I can run through it for people watching the recording as well as just for your input as well. But the only thing left is this distro version.
This was supposed to be like our our patch release. And right now, like the the complaint was that, like our telemetry doesn't actually put the version of the the actual SDK, or I'm sorry of the instrumentation into any like telemetry. That's downstream, which is fair. And I think this is this is Ron's got a solution. It works. It definitely does. It's great because it can get imported from different places. The problem is, it doesn't work with our tooling.
This is just on the back of my burner, but I'll probably just submit something instead of changing this Pr directly to make it into a module to work with our multimod thing.
But yeah, I think that I think we're pretty close. I honestly don't think it's it's even critical. This is included in the release. I think that was another question I was gonna ask, but yeah, no big deal.
**Rafael Roquetto** 05:23 Yeah.
**Tyler** 05:23 Yeah.
**Rafael Roquetto** 05:25 From my end. I I did start looking at that pr from again, from from Mike, the the handlers one. But I I once talked to him. Actually, once he's back, I have to ping him, and and I know he's explained this maybe 12 times already. But I need to go over him again. I mean, the Pr. Looks fine, but there's a lot of implicit decision or rationale there. So I wanna go over it with him again, and and then I'll maybe have something productive to say. It's better than saying something just for the sake of it.
**Tyler** 05:56 Oh, a hundred percent. Yeah. And like, this one's been open for a little while. So I think, making sure that, like, you understand, it is kind of the key which is important, like, I think that's actually more important.
because I actually, I don't think that this iteration or previous iterations were wrong like. There was like a few bugs. But like like, that's not really the point of the Pr, it's more about the design and how we want it to like live in the long term. So, having a clear understanding and like understanding how but how you will use it, I think, is important.
which is kind of what we asked you for just to, you know, is this going to work? If you know we have a probe that looks like this, could we? Could we do something in like the Ob stuff that could could eventually like consume it? It's kind of the thing.
Yeah. Also.
Yeah.
**Rafael Roquetto** 06:36 Actually after the call, and maybe I can sit out with him. He can go over again. Then I can go over the Pr again, because I did look into it. But I was like, yeah, it looks fine. But I'm lacking context. I mean that page out of my brain. So I need to to chat with him again and
**Tyler** 06:54 Yeah, I know he I'm looking. He says he like might be a little late to the call. But yeah, I I think that that's kind of the key as well like I'm lacking a little context for how this is gonna integrate into ob like, I think I'm happy to provide more feedback, I think on like the actual design internal but I kind of like, want to get a something in my head to understand. Like.
okay, so like we, we do this change. I like, this is, this is again like you said, like, there's a lot of other changes that we wanted to do before we actually get this into a public space. But like once we get it into like a a public space like whatever that is like.
like, how does that look when it integrates with the the Ob project? Right? So like I, I need to. I think I need to understand what the Ob project needs first.st So I need to go. The reverse direction of where you're coming from. This is what it is. So.
**Rafael Roquetto** 07:46 actually, yeah, last time me and him talked about this was like months ago, and that's when I gave him a like a tour of how at the time Bela did it.
So. Yes, I'm interested on that, too, because it has it has to fit. I mean I I not that it has to fit the shoe, it'd be good if fit the shoe.
Yeah. So then.
**Tyler** 08:07 It has to like it has to. Because I we gotta. We gotta somehow integrate these 2 projects because I think one like our development efforts like it would be way more like, there's a bit more force multipliers there right like, if we can have development on probes in this project be used in that project like that's great. If we can have 3rd party probes developed to be used in both projects like, that's even better. Right? So then I think if there's there's definitely like.
because otherwise we're just working on 2 different things that are doing the same, the same job. So like we need to have some sort of unification strategy there, which is the whole point of of trying to get this donation to work. And so I think if that's that's that's key. And so I, yeah, what that, what that looks like in the end needs to integrate in both projects.
**Rafael Roquetto** 08:54 Yeah, I agree. And also, like as a bonus, for everything you've said is once we solve, we kind of solve that problem. Then we don't need to keep rediscussing it, you know. It's like it's done. We can polish it, improve it if you know, when we hit bump speed bumps down the road. But yeah, I agree with you 100%. So yeah, I'll I'll schedule a call with him this week. This week is a bit quieter, everyone, because we think we have hackathon going on so this time this time for that.
**Tyler** 09:28 Has anybody.
Is anybody going to the hotel community day for you guys.
**Rafael Roquetto** 09:33 No, not me, as far as I know where I don't. When is it.
**Tyler** 09:38 Friday.
**Rafael Roquetto** 09:40 Friday, is it like, it's like physical event? I'm not even aware. Yeah, yeah.
**Tyler** 09:46 Yeah, yeah, it's in Denver. It's like a observability day, maybe, or something. I always forget what they call them. But like, yeah, it was like a thing. Nicola and I submitted a paper to it, or a talk that didn't get accepted or no. It got wait, listed.
**Rafael Roquetto** 10:00 Yep.
**Tyler** 10:01 Which is the worst. So yeah, but yeah, I know Nicola is not going, and I was just wondering if anybody else from Grafana was. But yeah.
**Rafael Roquetto** 10:08 I don't know like I'm not going. And, by the way, next week.
on Tuesday I both me and Nicola are off because it's July 1st Canada day. So just a heads up.
**Tyler** 10:19 Oh, okay, yeah. That's a good point. If it's July first.st There, that's July. Oh, yeah. July 4, th next Friday. Okay, so yeah, all right. Good to know. Yeah, I forgot about that. Yeah.
**Rafael Roquetto** 10:33 Years is like flying by. It's oh, yeah.
**Tyler** 10:37 Yeah, it's already. It's already summer. Like, I like, it's just yeah. It's nuts. Yeah, all right. Yeah.
**Rafael Roquetto** 10:45 Tell me about it, and I haven't lost any weight yet since the the year started was like, Okay, this is the year, you know, and it's been 6 months and.
**Tyler** 10:53 Right? Yeah, I know it's tough tough to get after it, hey, Mike.
**Mike Dame** 10:57 Hey, guys, how's it going.
**Tyler** 10:59 Doing well.
We were just going through the the milestone and some other topics. We were talking about the the probe Api refactor as well, but we didn't have too much of an agenda today.
I guess maybe I can ask you this question as well. So I was looking at this milestone. I was trying to get this released before today. But going slow. Okay, what's going on there?
Yeah. So just this Pr was left this add distro version in the naming to the hotel. SDK, so the only problem I had was that it doesn't actually get supported by our tooling. And so I was looking at this. I think that if we just make this into its own module, and then I think, rename some of these like it should work just fine. I was going to make a Pr similar to like what the other ones that I've been working on. What's going on here. What are your thoughts on that? Just to replace this.
**Mike Dame** 11:59 Yeah, I think so. Ron's still out. He'll be back next week. But trying to get this little patch version out, I don't know what is multimod? I wasn't.
**Tyler** 12:07 2.
Yeah, it's it's specific tooling inside the openstelemetry, like space that we created to support. Like Monorepos, it essentially is the thing that works with this versioning our Versionsyaml file, which we have in the project right now and essentially takes that. And it looks through all of our. There's a few steps, it can actually sync with an upstream repository for things like contrib repositories, and then it can update all of the versions. So if, like, you go through this and, like you have interdependencies. So module A and B get updated at the same time. And they're different versions. Well, if module A depends on module B, like, you need to update that version in module A of B, so it's like trying to coordinate that across like 2 modules, not a problem trying to coordinate it across like 15 modules is like, it's not something a human can do without making mistakes. So like, that's that's really what it's used for. And of course, because of that, like a lot of tooling, is also built in for this sort of thing like, Hey, if you have a version file like we'll, we'll automatically bump these things for you. So this is what we use in our release process. And so it would just handle that for us. Essentially.
**Mike Dame** 13:17 Yeah, yeah. Makes sense that. You know, I can see that I never saw this tool before. But I'm I'm assuming it's using like the collector, and stuff for all those huge multi module repos.
**Tyler** 13:28 Yeah, it originated in the go. The open telemetry go project, and the collector did pick it up. We also use it in like the proto go any go like mono repo. We've used it in hotel. So yeah, it's it's also like super homegrown. So it's not like I wouldn't. I don't know if I'd recommend it outside of hotel like, if you wanted to pick this up internal to your company, or something like that, that might.
I might pause on that one, but that also means that like, if you ever do find bugs or things you want to change.
**Mike Dame** 13:59 We accept dramatic changes to this thing. So
**Tyler** 14:02 You know, we, we have full control over it essentially is how that looks at it. So, yeah.
**Mike Dame** 14:06 Cool. Yeah, I think I get the the basic reason what you're asking for here. So yeah, I think, if you wanted to replace this Pr with one that works with multimod. That was, that was the changes to make this its own module. So it'll work with that tool.
**Tyler** 14:20 Yeah, yeah, that sounds good. And so I'll I'll get something up to support that and then hopefully get that pull request up for the release would be ideal. Hopefully, I'll try to get that done today. We'll see. I've got a lot of things going on. But yeah, that's kind of the goal.
**Rafael Roquetto** 14:40 Oh, cool. So okay, go ahead. No, you you first.st
**Tyler** 14:44 No, I was going to point it towards you, anyway. So the yeah, go ahead.
**Rafael Roquetto** 14:47 Yeah, I was talking to Tyler about the your Pr. The the probe one the probe Api and I. I had a look last week.
But I thought it would be better if you know if you ever have time. Sometime soon, that we could sit together again, and you can walk me through the the rationales again. I know you've done that maybe a dozen times already, but you said you're really good at it. So I'm leveraging that.
**Mike Dame** 15:16 Yeah, no, that's actually, that's a good idea. And you know, I I think it would be good to have for me to to have a chance to sit back and take a a step back and go fully through it again. I actually was honestly even thinking of it might maybe be easier to just like start it from scratch again with everything that we've gone through and learned at this point, and kind of just have a fresh one, even if it ends up looking basically the same as what I have cause I would like to. I feel like the the more that it's been kind of like tweaks and changes, and it's kind of lost some of the steam and just become more overwhelming to review. So maybe what I'll do is try to just open a new pr, like looking at this and if it's exactly the same, then I'll just walk. You guys through this one, but it might just kind of, I think.
like the perspective of it. Kind of give everyone a little bit more motivation to go through if it was a fresh one. What do you guys think about that? Do you think that this one, you know, we could kind of look at this one and go through with it? Or would it be helpful to start fresh with it?
**Rafael Roquetto** 16:20 For me, I guess it. What would be more helpful would be talking to you regardless. But obviously, if you think you see value on doing a new one. Then then, you know, happy to do that, and I can maybe review it again in my mind process, and we can talk afterwards, so I think I think you know you're in better position to to make the call than I am.
**Mike Dame** 16:46 Yeah, okay, let's let's you know, Raphael, if you wanna talk, maybe tomorrow that'll give me a chance to go through and make sure that I do actually understand it all like before I because I same way with me, like I've been explaining the general ideas, but I haven't given it a a full, fresh look through as I've you know, been kind of hitting it from from every every side that got some review. So yeah, let me look at it tonight, and we can chat tomorrow and go over it. I think. You know the general idea should be pretty simple for it, but then it's you know, it's kind of the devil in details.
**Rafael Roquetto** 17:22 Yeah. Sounds good. Sounds good. We could do that yeah, tomorrow morning. It's always a bit. I mean, I have some windows in terms of meetings. There's the Ubpf. Meeting afternoon free. But you know, see what works for you, and then we can work it out. We can. We can talk about it on slack, though.
**Mike Dame** 17:39 Yeah, if if you're free after the like, right after the Ebpf meeting, I could do that.
**Rafael Roquetto** 17:45 Yeah, let me have a look.
Oh, no, I have these c plus plus seek afterwards. Attend. So
**Mike Dame** 17:55 We can work it out.
**Rafael Roquetto** 17:55 But after, after like, after the hour after the Ubpf meeting, I'm free anytime. So.
**Mike Dame** 18:02 Cool, and I'll.
**Rafael Roquetto** 18:03 Send me an invite.
**Mike Dame** 18:04 I'll sync up with you. Tyler, would you like to go over that Pr. Too? Or do you think you're.
**Tyler** 18:10 I would. But I don't think I have time tomorrow. Yeah. So I know I don't know.
Yeah, I mean.
**Mike Dame** 18:18 Me, and Raphael will kind of peer review it tomorrow, and then we don't need to waste your time, too, with it, in case there's stuff that we find that we think we should change, and maybe we'll.
**Rafael Roquetto** 18:28 Hmm.
**Mike Dame** 18:29 Let you know how that goes, and you know, try to present a cleaner version for you.
**Rafael Roquetto** 18:35 Yeah.
**Tyler** 18:36 Yeah, I'm interested in all of it. So yeah, yeah, go ahead.
**Rafael Roquetto** 18:40 I was just gonna say, looking here like, yeah, my morning inspect tomorrow, like, I forgot, there's supposed to then have another community call so afternoon would be better anytime in in the afternoon.
it's now 1050 am. For me, so I don't know the time zone difference. But anyhow, you get the idea. We work it out.
**Mike Dame** 19:00 Yeah, I'll I'll send you a thing on slack and tell you. You know we we can work something out.
**Rafael Roquetto** 19:06 Yeah, sounds good. You can do even tomorrow morning. We keep in touch. Yeah.
**Mike Dame** 19:10 Cool.
**Tyler** 19:13 Well, cool. Yeah, I'm kind of bummed. I can't join, but I am jam packed tomorrow.
I'm looking forward. I'm looking forward to the to the follow up as well. So I.
**Mike Dame** 19:24 I'm excited.
**Tyler** 19:25 Rehearsal.
**Mike Dame** 19:25 I think that that will be good, so that me and Raphael can kind of have a breakdown like we're. I'm not just gonna explain it to you, Raphael. I think that's gonna kind of be an interactive like, let's let's review it and break it down and kind of like try to make some progress on it, and then that saves Tyler some time to anyone else that needs to review it. So we'll just take on the the hard work of shaping it up, and I think that that'll kind of make it a lot more presentable.
**Rafael Roquetto** 19:49 Yeah, sounds good.
**Tyler** 19:51 Awesome.
Well, that's that's really exciting. I'm really happy to hear that we're making some progress on this. So thank you both for taking time. Yeah.
**Rafael Roquetto** 19:59 I just don't know the hard work.
**Tyler** 20:02 He is actually yes.
**Rafael Roquetto** 20:04 Yeah, yeah.
**Tyler** 20:05 Well, awesome. That's the end of the written agenda. Any other things I did see. Oh, yeah, I was looking randomly. I think that the open telemetry observability day at Kubecon, North America, Cfp. Is still open. Believe it or not, I think, till the end of this week I might have misunderstood that, but I think it like I knew it was always a little later. But it's specific for the observability day right now. So if you did have talks that didn't get accepted at the Kubecon, North America.
or I guess that hasn't been announced yet, or any other place that you wanted to give a talk at. I think that there's still proposal things I did want to mention. But yeah, also, maybe just double check me as well, because, like, it seems odd that it would still be open. But I don't know.
**Mike Dame** 20:54 It was super late that it opened up like I thought you meant the Open Source summit that's happening this week.
**Tyler** 21:00 Oh, that's why I was like, no, yeah, no way.
**Mike Dame** 21:04 Yeah, this was, I think it was like until at least mid June that it's open for.
**Tyler** 21:09 Yeah, I was looking at it yesterday because I was looking at like the the dashboard, for some reason, and I like saw that it was still open. So yeah, I just if if you haven't, if you have a harebrained idea like, submit it because I think the successful like hotel observability days that I've been to are the ones that have the most hotel talks at them. So I'd love supporting people to give hotel talks there. I think it makes makes a big difference for me, at least, maybe that's just biased. But yeah.
well, cool. Any other topics people want to talk about before we jump off here.
Awesome? Well, if not, we can end it here. Good! Seeing you all. I look forward to the the follow up from that meeting tomorrow, and I will see you all in a week's time.
**Rafael Roquetto** 21:58 Yeah, I mean, forget. July first.st We're off.
**Tyler** 22:00 Oh, yeah, I will see you in 2 weeks. Yeah, yeah, right?
**Rafael Roquetto** 22:03 Alright! Alright! See you.
**Tyler** 22:05 Alright, bye.
**Rafael Roquetto** 22:06 Bye.
