SIG: CI/CD SemConv SIG
Date: 2026-02-17
Duration: 43 minutes
Zoom Recording URL: https://zoom.us/rec/share/CWsCudLzppbiazwnSpy8SEjNkqigp1xQ6oVopmfiA5q_pJmpUsiQcdFUmVlEw9gK.MRCpUYvDo9ECzgsj
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:16 Hi, Alan, how are you?
**Alan Clucas** 00:18 Hello, I'm alright, how are you?
**Christophe Kamphaus** 00:23 I'm fine.
**Alan Clucas** 00:24 Good.
**Christophe Kamphaus** 00:42 I saw that a few people can't make it today.
**Alan Clucas** 00:46 Yeah.
**Christophe Kamphaus** 01:16 I saw the recording from last week.
I think you had a nice discussion about… So your long-running spans.
**Alan Clucas** 01:26 Yeah, it was… That was useful.
Yeah.
I, the other thing I've done since last week… I haven't finished that PR for Go Contra for the environment propagator.
But I have replaced my environment propagator in Workflows, which is not in Workflows yet, but in my PR, or Tracing Workflows, is replaced by that one exactly, so… Proofs it works for me.
**Christophe Kamphaus** 01:57 Good to hear.
**Alan Clucas** 01:58 So, yeah, once it's actually upstream, I can just import it, but… Yeah, the only thing I need to do there is, like, enforce the… read once semantics, I think. I haven't done that yet, but…
**Christophe Kamphaus** 02:16 So that, yeah.
I remember the discussion right, then another point was the length.
And whether we should enforce the limits there.
But I'm not sure if it's already done.
In the libraries that we use.
**Alan Clucas** 02:33 No, there's nobody so far, as far as I can tell, enforces the limits, it looks like.
The expectation is it's on the… on the caller to… To do it.
**Christophe Kamphaus** 02:44 So basically, it's written in the specs, but no one actually does it.
**Alan Clucas** 02:49 Well, yeah.
That's what it seems to me. I haven't finished it. Yeah, that was to do as well, but yeah.
**Christophe Kamphaus** 03:00 Yeah.
While watching the recording, one thought I had.
was… We can send events to update the attributes of a given span.
But how often would that actually happen?
As far as I… know about, it's mostly you just initialize the spend, maybe you set one or two attributes, but then it stays the same, more or less, until it's done. And then maybe you set some result attributes.
And that would be it.
**Alan Clucas** 03:38 Yeah, my… from my point of view, I don't mind. From my use case, I could set… I could do all attribute setting at the end.
The downside of doing that is you don't… if you want to do the observing whilst it's running, you don't have the attributes then.
So, where they're non-result attributes, that's… Bad, but from an implementation point of view.
the… I think the implementers don't want to have to do It becomes hard to generate… it becomes a lot more complicated to generate a span if you're having to observe every intervening… event.
So, I'm…
**Christophe Kamphaus** 04:23 Yeah, for sure, and then you would need to merge… Any attributes in between?
**Alan Clucas** 04:29 Yeah.
I mean, and then… is the expectation that you could, like… I mean, somebody might think, oh, well, I could just, like, I could put a progress bar in as an attribute, and that obviously can't happen, really, but… It feels like you could do it if you're allowed to.
Excellent.
**Christophe Kamphaus** 04:47 Keep updating, on that.
**Alan Clucas** 04:48 Creating an attribute and saying, you know, we're 10% done now.
Yeah.
I mean, that would be a… so I think we should try to prevent that kind of behaviour. Maybe just start and end should be allowed to contain.
Updates and anything in end overwrites anything in start.
**Christophe Kamphaus** 05:09 Yeah, and then the in-progress event would just… maybe have the ID of that event, just to refer to it.
And keep it up to date, in progress, basically.
**Alan Clucas** 05:22 Yeah, it's basically to say I haven't given up.
**Christophe Kamphaus** 05:26 Yeah. That's my…
**Alan Clucas** 05:27 my take on it, it's just like… so that an event that can eventually be closed if it hasn't been heartbreed in long enough.
**Christophe Kamphaus** 05:36 And it makes sense to already send attributes in the first event.
Because maybe you need some in your UI to show it belongs to this job, it's this commit, and so on.
**Alan Clucas** 05:46 Yeah.
**Christophe Kamphaus** 05:48 Yep.
**Dotan Horovits** 05:57 Hey, everyone.
**Christophe Kamphaus** 05:58 I don't.
**Dotan Horovits** 06:02 I took the liberty of adding you, you were in the middle of a conversation, so just added your name there on the talk, too.
Save you the time.
**Alan Clucas** 06:10 Oh, thank you. I haven't done… yeah. Thank you.
**neil yashinsky** 06:15 Also, good morning, everyone, or good day.
**Christophe Kamphaus** 06:17 Good morning.
**Dotan Horovits** 06:18 I knew.
**neil yashinsky** 06:19 How's it going?
**Dotan Horovits** 06:19 Good morning.
**neil yashinsky** 06:20 Good to hear you.
**Christophe Kamphaus** 06:22 Sorry, we started the discussion without you. We continued the one from last week.
I just watched the recording yesterday, and so it was fresh in my mind.
**neil yashinsky** 06:34 Oh, by all means, yeah.
I'm excited to, to hear what's, what's going on. So, did I miss anything important, Dr. Stuff?
**Christophe Kamphaus** 06:45 Basically, our conclusion was we might want to send a start event with all the attributes.
**neil yashinsky** 06:52 You could.
**Christophe Kamphaus** 06:53 already displayed in a UI.
And in the end event, you would also send again all attributes, plus in case anything changed in between.
Or you said a result attribute?
But then for the heartbeat, maybe you just want to send the event ID, Or suspend ID, so you know exactly which… Spent to keep alive.
**neil yashinsky** 07:19 Right, right.
Mark Zepler, I guess.
**Christophe Kamphaus** 07:23 That way, you would not need to, care about any… Attribute, merge, semantics, you just know.
Start attributes, end attributes, and see end attributes, just replace the one from the start.
**neil yashinsky** 07:39 Yeah.
And it seems that's very clean if it's, like, the most important thing you're trying to do.
Infer… not infer, You know, determine, I guess, or whatever, the health of the job itself.
And so that's why the data's centered on that. Seems smart.
**Dotan Horovits** 08:02 Christophe, would you mind, maybe just capturing? This was a good, follow-up for last week's, if you want to make sure that we capture that on the meeting minutes there as well.
**Christophe Kamphaus** 08:12 Yeah, I will, write it down.
**Dotan Horovits** 08:15 That'd be good. I shared, by the way, the meeting doc in the chat for those who want a quick link. Feel free to add yourselves, and also add agenda items for the meeting.
And actually, Christophe, would you like to take us through the triage? I think you'll be.
**Christophe Kamphaus** 08:40 Short.
**Dotan Horovits** 08:41 I can do that.
**Christophe Kamphaus** 08:43 Give me a second.
**Dotan Horovits** 08:44 Sure.
**Christophe Kamphaus** 08:53 Here we go.
I don't see anything having changed.
I also didn't see any notifications.
Before you joined, Alan also gave a quick status update about the Go implementation for… the environment variables…
**Alan Clucas** 09:26 Yeah, I'm… I haven't done much work on it, but I have adopted it in other workflows in my tracing undone PR, and it works great. So, yeah, proving that it works.
Yeah, there's a couple of things that still need addressing in it, though.
**Christophe Kamphaus** 09:48 I don't see anything having changed here, nothing new, so… I think we can conclude.
the triage part.
**Dotan Horovits** 09:58 Sounds good. Alan, if you want to, put a note about, your, recent experimentation, validation, sorry, with the, the Go, one.
Or if you think it's covered already from, yeah, previous notes, Well, well, just making sure I don't see any additional agenda items, making sure around the table, if anyone else had something, that'll be a great time to add your… Items to the list…
**Christophe Kamphaus** 10:40 No update from my side regarding the Jenkins PR. I was booked on with work, so I hope to get to it.
Sometime soon.
**Dotan Horovits** 10:50 Is there any dependence in terms of the team there, or do you feel.
**Christophe Kamphaus** 10:55 No, it's just on myself.
**Dotan Horovits** 10:56 thing is… Oh, okay.
**Christophe Kamphaus** 10:58 Yeah, I had the handover with the Jenkins developers, so… That went very nicely. I also talked with, Ed Foster, so…
**Dotan Horovits** 11:07 Yeah, yeah.
Autel Unplugged, yeah, yeah. I told them that, if there's anything that, they can do to, to enable this, conclusion with, obviously, with Euro taking the lead, but anything that they can help us, we'll be happy to, Get this, wrapped up.
Great to hear, Scott.
That'd be great. I think, actually, it's going to be the first, like, proper implementation that is going to be, like, the native, the emission, right?
**Christophe Kamphaus** 11:41 As far as… At least behind the feature flag.
**Dotan Horovits** 11:45 Yeah, that's, technicalities of how you enable it, but the fact that a tool, emits… emits that as a first-level citizen, rather than resulting to a collector stage, you know, conversions, transformations, attribute mapping, or things like that, I think this would be, A great win, and hopefully a good, reference that we can then take with, with, with others, so… Ideally, I would like to have it in March.
**Christophe Kamphaus** 12:18 before KubeCon, but, yeah.
**Dotan Horovits** 12:21 Yeah.
**Christophe Kamphaus** 12:22 Let's see how it goes.
**Dotan Horovits** 12:23 That'd be amazing, and And I definitely want to use, KubeCoin, and I had the chat with, with the folks from the… the GC, Autel GC, about, getting, once… once they get the… schedule or whatnot for the, observatory, that we want to slot for the SIG, and, so I mentioned that to, Ted Yang, and I think to Lyudmila as well.
So, yeah, that'd be great to… first, having this slot, and if we can highlight that, that'd be, even… even more impressive, because this hopefully can seed additional conversations around that. I also had some interesting conversations at, at NDC London, with, someone from the, from the, I guess, sort of OSPO team at, at GitHub, trying another angle.
to tackle, GitHub and see if we can bring him to the… to, take part in this initiative.
So, and I had some discussion with folks from GitLab at, at first, again, they're from the open source side, but trying to see if they can bring the relevant folks to the table, and followed up with some reference material about what we've achieved so far, and so on, so… I still haven't given up, at least on finding… getting these vendors to take part.
And I'm saying that once we have one tool that is… established tools such as Jenkins, having that as a first-level citizen, that'd be, I think, a very, very good reference point for others.
**neil yashinsky** 14:06 Yeah, that makes sense. It'll kind of create, what is it, gravitational pull or something like that, or some sort of, it's not the right words, but I think I… you don't intercept 100%.
**Dotan Horovits** 14:17 Yeah, yeah.
**neil yashinsky** 14:17 For sure.
**Dotan Horovits** 14:19 Yeah, and anyway, it's… obviously, it's open to anyone who has some connections that feel that they can, get some more conversations around that from other angles. These are huge organizations, so feel free, whether independently, if you want to ping me, and we can sync, or whatnot, as long as we get some more eyeballs on this, and get more… Traction, so, that's always good.
**Christophe Kamphaus** 14:48 Nice to hear that.
Did you have any, conversations at Hotel Unplugged at Fosterm?
**Dotan Horovits** 14:55 So, I actually brought up, SamCon more broadly, not just, CICD and the… it's a non-conference, for those who don't know, so essentially, people just suggest topics, and that, based on the gravity of topics, the top ones are being chosen and become open sessions, essentially. So, there was a session… Elected for, about, about, SAMConv in general.
That I attended. Ted Yang was also there, and it was very interesting because a lot of the people who came to the session were actually end users, or folks that are trying to use, which is great, for me at least, to understand we're at the cutting edge, bleeding edge, but understanding that people are struggling, even understanding, what, in the SEM corn, navigating different SEM corners, like, where do I find which, how do I engage? It was very interesting. Obviously, I used the opportunity to share about this specific SIG, for those who weren't aware. Also, I'm also involved in the service and, and deployment, semconvs, so this is an even newer one, so, share that. It was very interesting, like, folks were saying, hey, I'm looking for where to put my… the owner name.
on attributes that say, hey, this is being discussed as we speak at the service and deployment SEM conference, like, how about you join the discussion? And so it was really nice to see, on the one hand, that it is a need, like, a very, very concrete need.
And secondly, on the other hand, that we have a lot of work to do on making it, I guess, more accessible.
to the wider audience, so while many of you do the coding parts, I'm trying to take the part about spreading the word and getting the knowledge share.
**neil yashinsky** 16:58 And and there's a lot to do there, so it was eye-opening for me as well, and .
**Dotan Horovits** 17:04 That's why I'm actually… I was hoping that Adriel would be here, but I'm pushing to have, like, another blog post for me and Adriel, by the way, if anyone else wants to join.
I'm happy to do that. I know that you're taking a load on another front, so I don't want to burden anyone, but, like, using the opportunity of the Phase 2, to, again, resurface the, the SIG, show what's been achieved in Phase 1, and the finishing with a call to action for folks to join us in Phase 2, including, by the way.
the tool owners and vendors that implement also adopt and implement, so not just, even if it's outside the SIG per se, but, like, adopting the SEMCOM, so, This is another goal that I have for that part. And yeah, at KubeCon, that would be the next, big opportunity to, get together. Us, firstly, and secondly, hopefully have an inter… at least as an interesting discussion as we had. Alan remembers that at, at KubeCon, What was that, London?
that, right?
Yeah, so, so, something like that.
**Christophe Kamphaus** 18:21 Yeah, I also had some very nice conversations at KubeCon Paris.
**Dotan Horovits** 18:25 Yep, it's always a good opportunity.
Also, again, other maintainers in other parts of OTEL, because, you know, we have the dependency on SDKs, so… smoothen things up and seeing how, if they need some help, or how they find adopting and implementing, and also with getting the TC folks more engaged and others, so it's really a good place.
Interestingly enough, I just saw a PR from the Gen AI… related to the GenAI SIG, which was interesting because they've been struggling with something similar to, to, what we had, like, with GitHub and GitLab, because they have, like, open inference, and then they have open LLMetry.
And both of which are much more mature than what the OTEL SDK supports, so many go result to these, but each one has its own convention, and each one supports, like, 30-plus LLMs.
So, actually, there was a proposal, I… I know the, actually, the contributor, of actually making, like, a processor that will be, doing the, the transformation, sort of the, I forgot the word that he used for that, but sort of to, normalize, like, normalize the, yeah.
Exactly. So, it was interesting, I commented on that PR, saying, hey, actually, we had a similar challenge in CICD, and we actually took the path of having a receiver per vendor.
which, to me, made a bit more sense maintainability-wise, because it's more well-encapsulated. Like, you have one receiver per vendor, which, A, if someone from the vendor wants to join, it's very well encapsulated, they can only zoom in on this part. And even if someone is not from the vendor, but is hands-on with, let's say, GitLab in our case.
They can go dive deep and go into that, whereas if you put one processor that's supposed to be doing normalization across several.
it may be more intimidating or, you know, make it a bit… higher the bar to entry, the barrier to entry to start. So I just brought it up as a point of thought for them.
But interesting to see, again, other, other folks, Looking into how you go about getting the adoption while the vendors still don't support your, like, chicken and egg thing.
and breaking this cycle by having your own intermediary, like, collector phase, until you have the native support natively emitted by the vendor. So, just sharing that also, if you have other insights that you want to share with that SIG or other SIGs.
**neil yashinsky** 21:16 That's a good point, Dotana. I think it just… it just resonates with me very well against a lot of the… You know, the SIGs that I've been interacting with are interfacing with the very, very same challenges, or, you know, similar challenges. And I like this approach for what it's worth, because I think it kind of meets people where they're at. I think inherent in our work is a little bit of, let's say the… naive optimism of, I'm gonna say nerds in the best sense of the word, that, like, if you build a better mousetrap, the world will, you know, beat a path to your door, and… That's definitely not always the case. In fact, it's probably rarely the case, even. Technology implementations at least have some pain that we can solve, but that still, like, doesn't do the work of spreading the word, really. Or convincing people to adopt, even.
**Dotan Horovits** 22:11 No, it's, definitely, that's the case, so, Let me look while, at it if I find the, gen AI…
**neil yashinsky** 22:21 And while you're looking, I'll just say that the Blueprint team is really coming up on some of the interesting intersections of, like.
what is a technology versus what's a, you know, like, vendor-specific things that are above our pay grade, quote-unquote, or whatever, to use an English term. But, like, Yeah, I feel like, to be most useful, we don't want to simply work in abstract. And I'm not saying we are, it's a straw person of sorts, but there's a danger in just speaking to the abstract without… getting into the real-world challenges people face and why they need to use this. Which is why I love the Blueprint, it's kind of like a little bit of an interface between those two fields.
**Dotan Horovits** 23:02 Yeah, I agree. Actually, just to make sure, is everyone here around the table familiar with Blueprints? It's pretty new, so it's okay if you don't, it's very, very new.
Yeah, so let me share that, it's, great. By the way, any… this is, like, diverging from the core of the… happy to take the time, but just want to make sure if anyone else has other, more pressing agenda items, happy to deprioritize this one more for.
**Christophe Kamphaus** 23:24 No, not from my side. I was just wondering if anyone at the end conference mentions, Multi-registries, the distributed registries of some kind.
**Dotan Horovits** 23:38 and noted the con… another conversation that I had. Let me… I found the PR, by the way. This is the issue, sorry, issue, but he has, like, already the blueprint of the implementation on his own repo, Kyle, so it's, an issue, but he also won't… has the code. Anyway, so, You know, before going to the blueprints, I just want to conclude. So, essentially, that was a very good discussion on SemConv, and first of all, the fact that it was elected means that there was a lot of, interest in learning from different angles around SEMCON, so I was happy that this topic was elected as a session in the first place, and then the discussion was very good.
And about the blueprints, which also, by the way, had its own session, so it was another interesting part. So essentially, it's Dan, that we know very well here.
in the group, he was our, our, mentor from the TC until, recently. So, he actually initiated the, the blueprints, which… Should give, sort of, like, looking at the end users, lowered the barrier to entry by, taking these common use cases of putting OpenTelemetry to use, and creating blueprints around it, so opinionated blueprints of how it should work, so… We have some docs, lots of to-do about docs and things like that, but something, like, more zoomed in than the broad docs that gives you the whole spectrum and variety of ways to use it, and actually take something more opinionated and more focused, let's say.
think about, obviously, the clear thing is about running on Kubernetes, of course, and cloud-native, and, like, containerized, but also think about, like, more traditional environments, such as VMs.
or, or, bare metal, you can go as far as, I guess, mainframe, if you will.
**neil yashinsky** 25:39 Yeah, let's do it.
**Dotan Horovits** 25:41 So that's, like, in a nutshell, the idea of Blueprints. It's still a proposal, so it's early on, and if you want to chime in, I think it's a good time to… feed in with what you found to be, pains or use cases that should be covered with a blueprint, and how… what should encompass a blueprint. This is, definitely something that you can… you can chime in on. But just so you'd know, so, and obviously, with blueprints, I definitely see a room for baking the stem cores into the blueprint so that it makes it easier for folks to start already from the get-go, already be aligned with Blueprints as much as… sorry, with SEM conference as much as possible when starting from the Blueprint. So, I want to pause here, and Neil, sounds like you've been following this as well, so if you want to add your take on this.
**neil yashinsky** 26:34 Yeah, yeah, thanks. I've had, yeah, I think what's really interesting about them is, in some ways, they're really starting with the process of, like, what's important for the blueprint to contain, irrespective of technology. And it has, I think, given us the perspective that, like.
there's a… there's a very cut-and-dry view of, like, technology as, like, oh, it will just get implemented in a sort, and, like, it precludes, or it doesn't include the fact that, like, people have to come to this decision path, and so I… I love the approach of, like, people are trying to solve this problem, you know, rather than, like, oh, I want to implement OTEL, they're like, hey, I need to, you know, make sure my queue… Kubernetes-based application runs well, and the resource kind of, you know, serves as a great entry point.
And so, yeah, I think you did an excellent job covering it, and Yeah, they just, I think, have… have… or, I guess we… I've contributed a little bit to it, in a non-code fashion, which is also another great thing, I think, about this, is, like, people who are like, oh, I… I'm not ready to write a bunch of code for OTEL, not that that's the only way to contribute, but this is, like, really good process stuff.
And I think people who have a lot of, you know, operational expertise will just be able to validate the format and the, you know, the approach of.
of making this type of content adjustable in a new fashion, or maybe for… maybe not necessarily a new audience, but I think in some ways, you know, one important suggestion that I… well, I would like to believe it's important, I don't know if it is important or not, I guess the jury's still out on that, but like… I feel like, secondary audiences, are a great way for us to get in front of more eyeballs, because they're trying to solve, if you will, the business problem of, you know, maintaining high availability for their customers, or etc.
And so, if we make this type of thing discoverable to them in a non-technical perspective or, you know, sense, then they can then pull in their appropriate resources, and it creates another mechanism to draw attention through You know, others still very related, but not exactly the same technical audience that we talk with every day.
**Dotan Horovits** 28:50 Yeah, definitely.
**Christophe Kamphaus** 28:54 Is it these ones? I found the project description and project board.
**Dotan Horovits** 29:00 Let's see…
**neil yashinsky** 29:03 Yes, that's it.
Yeah, so I think, 246 and 247 is kind of like… oh, well, I mean, 235 is the blueprint itself.
So, Yeah, I don't think we're the fastest, SIG quite yet, because I think we're… we're not… it's not boiling the ocean, it's more like, For people who… it's, it's, it's, it's the first, I don't know how many other, like, non-code SIGs there are that we can lend upon to, like, their process-oriented sigs, or documentation. I mean, obviously, we got documentation through the roof, or whatever, but this is like a… This is, like, operational documentation, which, you know, everyone on the call, please correct me if I'm wrong, but I don't really… OTEL is not synonymous with, like, operational insights, for me at least. I don't know if you maybe have… I mean, in a sense it is, but, like, it's only specific to the standards themselves, I suppose, versus, like.
I mean, I guess that's oversimplifying it quite a bit, but maybe my point is still clear in, like, this is… this is… About the operationalizing of technology more than the standardizing of technology itself?
And that's why it was an interesting intersection, just to finish up, is, like, there are some things that will be vendor-specific on this. And, like, how do we, as a SIG or a community, want to, like, or what's the right, you know, place to draw the line in terms of, like, hey, this is a proprietary implementation.
And even in that instance, be like, 4 more resources, you know, how do you want to… Point people to… if you will, vendor-specific wisdom on this issue, if at all. That's kind of still an open question. You know, is it… is it just like, here are the things to consider? Anyway, it's a really good effort, and I'm, excited to have a chance to have a front-row seat, even participate a little bit.
**Dotan Horovits** 30:58 Nice, good to hear that you're involved there. In that context, we should also maybe mention Weaver, project. Yes. So, again, just to make sure, is anyone not familiar with Weaver? I'm happy to say a word about that.
Don't be shy.
**Alan Clucas** 31:14 already. Okay.
**Dotan Horovits** 31:15 So, so Weaver essentially is a way to, I guess, add your own organizational semantic conventions, which… that's why it reminded me, when Neil said what he said, so… in a way that will sort of extend the out-of-the-box semantic conventions, then apply them in a systematic manner. I think the… the buzzword around that is, like, do it by design. This is, like, the slogan, so… I think it's interesting for us to know, because this, again, operationalizes the way that organizations may, more easily adopt, SEMCOMs across the organization in a uniform manner. So, I'm just looking to share the link.
**Christophe Kamphaus** 32:01 basically how you define distributed semantic conventions. So each vendor could define their own conventions.
That are specific for their products, and others could then consume those as well.
It is not only for internal… Conventions, but it's also, if you have a product.
And you want to provide open telemetry from it.
Here's how my attributes, my metrics are named and structured.
**neil yashinsky** 32:32 Yeah.
**Christophe Kamphaus** 32:32 And then an open question is, how could… OpenTelemetry, point to those vendor-specific conventions.
I think maybe, at some point, registry will be set up.
Like, the F4s or stuff.
**neil yashinsky** 32:49 Yeah, I just started sitting in on the… on the Weaver SIG, And, I plan on implementing it myself, actually, it's my… I've just started on it, for… for the software that I'm working on. And, because it provides a semantic layer around things, that's why, honestly, without getting into the details, which I'm happy to do, but without, you know, without a specific ask, I won't. But yes, because the Weaver creates this, almost an implementation layer, an abstraction, as well as tracking mechanism.
So you can see, you know, what percentage of things are implementing, and yes, automate the implementation, and… Yeah. Extend it with your own way, so… I've just started, Investigating that, and it seems like it's got a lot of value.
**Christophe Kamphaus** 33:39 Yeah, I tried it out myself as well.
**neil yashinsky** 33:41 Hmm.
**Christophe Kamphaus** 33:42 basically just copied the SAMconf repo and the Java library People to generate my own stuff.
**neil yashinsky** 33:52 Huh.
**Christophe Kamphaus** 33:52 So, definitely, how you can use it, can still be improved.
**neil yashinsky** 33:58 yeah, yeah, it's super early, and I… I wouldn't call it stalled as much as it's like… it's, like, one of those things, that people are… are… Having to do a lot of manual work in the interim.
It's gonna save people a ton of time, but it's not had the resources, ironically, to, like, make that happen quite yet.
So, that's, you know… Classic standard stuff, I guess.
**Christophe Kamphaus** 34:22 Yeah.
**Alan Clucas** 34:23 Okay.
So this… allows you to… I'm just catching up with what Weaver does, but effectively, you can define what Telemetry you emit.
Like, your attributes and your metrics and spans.
Perhaps. And then this does some… generation for you as well, is that correct? Because it looks like something… You could.
mentally.
**Christophe Kamphaus** 34:52 A library with circumstance for your project.
Or where you define your own, Signals… And use that in your project. That way, you are also sure that you are using exactly the ones you defined in SAMConf for your… yourself.
**Alan Clucas** 35:11 So, yeah.
**neil yashinsky** 35:13 Almost like a…
**Alan Clucas** 35:14 I've… I've… I've… I've… yeah, I did… I've already done this, basically, for workplace, because… so I will have to adopt Weaver now.
**neil yashinsky** 35:22 Yeah, exactly!
**Alan Clucas** 35:22 Exactly.
**Dotan Horovits** 35:23 It's not that you eat, you'll have to think about it, you don't Maintain this, this boiler.
**Alan Clucas** 35:28 Great thing.
**Dotan Horovits** 35:28 You have the community to do it for you.
**Alan Clucas** 35:30 Exactly.
**Christophe Kamphaus** 35:31 You can write some tests with Weaver to verify that what you actually emit is…
**neil yashinsky** 35:37 Yeah.
**Dotan Horovits** 35:38 Compliant to your own conventions.
**Alan Clucas** 35:40 Right?
**neil yashinsky** 35:40 Do the matching, and then do the replace. Yeah, yeah.
**Alan Clucas** 35:44 Does it do, I don't know whether everybody knows, does it do span parentage?
that's the thing that I've particularly… I've written in my… top-level document, I have written what spans are… have what parentage, so that then when I get… when I run a full end-to-end test, I just grab… I scrape the resulting span tree and ensure that it matches my spam parentage that I've documented. And then I can generate, like.
mermaid diagrams for my span parentage, and so people can understand what spans are expecting.
**Christophe Kamphaus** 36:19 I would bet that it does not, but it would make for a great GitHub issue.
**Alan Clucas** 36:24 Yeah, alright.
**Dotan Horovits** 36:26 Yeah.
**neil yashinsky** 36:26 Forever.
**Dotan Horovits** 36:27 RFC around that.
**Alan Clucas** 36:29 Yeah.
**neil yashinsky** 36:30 It might be on the roadmap already, because I've seen at least one other SIG, they're like.
Well, frankly, I was like, hey… it was almost embarrassing, honestly. Forgot which one it was, maybe it was the system one, and I was separating them, like, oh, hey, did you ever hear this, Weaver project? And he's like, yeah, Josh or whoever is the project, he's like, I work on his team. I was like, oh gosh, I'm so embarrassed. But then he's like, it's not ready for the thing that we could use it for yet.
like Alan just pointed out, it's almost like you either have already built a weaver yourself, or you're about to at some point in time if you get serious enough, or… and then eventually, of course, you realize it's just better to adopt a weaver, because why would you want to recreate this?
But again, I don't know if it's quite there yet. Certainly on that point, Alan, I don't think it is, but…
**Alan Clucas** 37:16 No.
I did it because I was fed up with finding I'd done it wrong.
**neil yashinsky** 37:21 Haha, exactly!
**Alan Clucas** 37:22 I generated everything so that I could ensure that what I've documented was actually what came out the other end. Yeah, yeah.
**neil yashinsky** 37:29 Out of necessity, right, right, right. Like all good software.
**Alan Clucas** 37:36 I'll have to have a look.
Thank you. Yeah, of course. I'm getting lots.
**neil yashinsky** 37:41 You know, we're on the border, I feel like maybe one or two more weeks, Alan, it'd be interesting to catch up if you're interested, because I do think there might be some value from what I'm building into what you're doing, and the implementation should be really light, so if you're interested in talking more about that, just let me know.
**Alan Clucas** 37:58 Yeah, sounds good.
**Dotan Horovits** 38:06 Anyway, so that's just a bit of updates and good thing that we're discovering nuggets within OTEL that we should make use of and connect the dots between different contributors and maintainers and different initiatives, so that's the power of these conversations. Yeah, sorry, go ahead.
**neil yashinsky** 38:23 No, no, no, I was, I was just following up, I don't know if, how common the phrase show and tell is outside of the U.S?
But it's like in show and tell in primary school, you, like, bring a fun toy from school or whatever, and you can just show and tell. It's very simple. Just talk about something that you like or whatever, and I kind of feel like… Some oat… every once in a while, some oh-tel show and tell is a really good thing, because we're all working, hopefully, on interesting, relevant, useful topics that have a lot of crossover.
And so, it's just, like, it increases the service area of the discoveries of topics and, you know, technologies and techniques, if we can, you know, like you just did, Dotam share. So thanks so much, Matt.
**Dotan Horovits** 39:03 Yeah, that's, that's really… when we have time, I think this is a great use of the time. I'm just going quickly, I had, like, on notes from the… from OTEL Unplugged to see if there's anything else about the, semantic conventions that is worth noting here.
there was discussion about the OBI, that's like the EBPF auto instrumentation, piece, another piece of Autel. So, the question is that someone flagged that OBI is currently meeting metrics that do not follow a semantic conventions, so… There was discussion about, like.
even within hotel proj… grant project or organization, to do this alignment. We know this pain with SDK, so it's also with the auto-instrumentation, with the eBPFI auto-instrumentation.
I'm looking quickly to see… there were some things that were brought up around database server side, things that are missing, difficult to find the service owner, I think this is what I pointed out about the service and deployment, SEMCON.
Hmm… questions about how to… how to contribute, discoverability, how to propose even a new SEMCON if you find the gap, because some people ask things, and they don't know if it falls within the realms of a specific SEMCON. We see that often, that someone joins.
**neil yashinsky** 40:37 And brings out.
**Dotan Horovits** 40:37 This is not that, but we redirect to the right one.
**neil yashinsky** 40:42 Yeah.
**Dotan Horovits** 40:42 This is sort of ad hoc, and luckily enough, many of us are connected to other SIGs and SEMCOMs and initiatives, but maybe more systematically how to do this discoverability meets the discoverability, angle. The, the deployment, blueprints, SIG, someone brought out, like, deployment blueprints, as a, like.
another way of, of, getting the SEMCONs more, more, integrated.
the stability, which was overarching topic throughout Hotel Unplugged Conference, but also in terms of specifically the SEMCONs, because it's like a chicken and egg. Some companies, I think I even brought it up that some companies don't want to invest unless it's stable.
And then, so it's… and on the other hand, we want the stability to… to be, like.
bulletproof, and how do we balance the two?
So, I know that we here are striving to, to get this, to get to this stability capacity, and I think it will be beneficial also for companies to adopt, in our case at least.
Mmm… I'm trying to think… Yeah, I think these are the main topics that came up on the discussion.
on that session.
Yeah, anyway, so, last, last round to make sure if anyone else has anything they want to, to discuss. If not, then, give you, I guess, 17 minutes, back.
**Christophe Kamphaus** 42:25 my slide.
**neil yashinsky** 42:27 Yeah, I'm good.
**Dotan Horovits** 42:28 Sounds good. So, keep an eye out for, for KubeCon. Neil, are you going to join? I know that Alan and Christophe are planning, but…
**neil yashinsky** 42:36 Where is it again?
**Dotan Horovits** 42:38 That's great, that's, KubeCon Europe, I mean.
**neil yashinsky** 42:42 Yeah, yeah, I, I…
**Dotan Horovits** 42:43 It's gonna be in Prague.
**neil yashinsky** 42:44 In Prague, I saw that!
**Dotan Horovits** 42:45 Yeah, sorry, in Amsterdam, sorry, sorry.
**Alan Clucas** 42:47 Absalom.
**Dotan Horovits** 42:47 Amazing.
**neil yashinsky** 42:48 Oh, Amsterdam. I think I saw it last week, and what's the date again?
**Dotan Horovits** 42:52 It's, let me check…
**Alan Clucas** 42:54 Last one.
**Christophe Kamphaus** 42:55 23rd of March?
**neil yashinsky** 42:56 Yeah, March. Yeah, I was… I was… it was, on the… it was on the board originally, but I don't think I'm gonna, quite make it happen. Fingers crossed, stranger things will happen. I really would love to be there, it'd be the perfect time.
But, yeah, I don't know if it'll be the perfect, perfect time. But, thanks a lot.
**Dotan Horovits** 43:14 All good, all good. No, no. If you have anyone else from your.
**neil yashinsky** 43:18 No.
**Dotan Horovits** 43:18 team, or folks that are relevant that are going to be there, and you want to connect us, anyone that has some passion to this, we're happy to have them there as well.
**neil yashinsky** 43:29 Absolutely.
**Dotan Horovits** 43:29 Yeah, love to.
**neil yashinsky** 43:30 Great.
**Dotan Horovits** 43:31 Anyway, so, thanks everyone, and, have a great rest of your day.
**Christophe Kamphaus** 43:36 U2.
**Alan Clucas** 43:36 Thank you.
**neil yashinsky** 43:37 See you. Cheers.
**Alan Clucas** 43:38 Dude.
