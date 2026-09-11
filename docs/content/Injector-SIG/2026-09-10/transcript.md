SIG: Injector SIG
Date: 2026-09-10
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 01:51 Hey, Zico.
**Michele Mancioppi (Dash0 Inc.)** 01:58 No, I think your microphone is dying.
There is a lot of background noise, the way that the microphones tend to have before they fail.
**Antoine Toulme (Splunk Inc.)** 02:08 My microphone? Yeah.
**Michele Mancioppi (Dash0 Inc.)** 02:11 There is a static background, static noise in the background.
**Antoine Toulme (Splunk Inc.)** 02:17 Oh, hang on… That's weird.
some Zoom stuff here.
You know, not work at Cisco, I'm on WebEx these days.
How about that?
**Michele Mancioppi (Dash0 Inc.)** 02:35 Much better.
**Antoine Toulme (Splunk Inc.)** 02:38 I had to turn on with musician stuff, apparently. I used it one time to make some music or something, so… No, it's just too much. Okay, alright, so let's go and get this, shown on the road. We got voting notes.
You know what to do, put your name in there.
If you don't, I'm happy to put your name for you.
**Michele Mancioppi (Dash0 Inc.)** 02:59 Yeah, can you please add mine also to the packaging? Because I'm from mobile.
**Antoine Toulme (Splunk Inc.)** 03:04 Of course, I just need to remember how many peas in Mancioppi.
**Michele Mancioppi (Dash0 Inc.)** 03:10 It has two P's.
**Antoine Toulme (Splunk Inc.)** 03:12 That's right. Okay.
**Michele Mancioppi (Dash0 Inc.)** 03:14 And one elf.
**Antoine Toulme (Splunk Inc.)** 03:18 1L? Yes, I got that.
That's easy.
Okay, you're in.
**Michele Mancioppi (Dash0 Inc.)** 03:25 By the way, you know Antoine, I still don't know how to pronounce your surname.
**Antoine Toulme (Splunk Inc.)** 03:31 Oh, that's a good question. There used to be a, It used to be an accent on the E at the end, so it's still… so it's still me. But…
**Michele Mancioppi (Dash0 Inc.)** 03:41 You know.
**Antoine Toulme (Splunk Inc.)** 03:42 my whole life I've had these names pronounced, so don't worry about it.
**Michele Mancioppi (Dash0 Inc.)** 03:48 So, you are going by Toulme in the US?
**Antoine Toulme (Splunk Inc.)** 03:51 Toulme told me…
**Michele Mancioppi (Dash0 Inc.)** 03:55 Mmm.
**Antoine Toulme (Splunk Inc.)** 03:55 Antoine sometimes also is being spelled with a W.
Because it's more fun this way.
Let me get a little grief.
**Bastian Krol (Dash0 Inc.)** 04:04 What?
**Antoine Toulme (Splunk Inc.)** 04:06 Yeah, I got my Starbucks once, and it says ANTWAN.
Right, so I have two emojis for my name now, it's like Ant and, Satellite dish.
Something like that. Antoine works well.
Yeah, so… Or, Antoine. People love to call me Anthony for some reason.
**Michele Mancioppi (Dash0 Inc.)** 04:30 infinite.
I have it almost as bad as I have.
**Antoine Toulme (Splunk Inc.)** 04:35 Not a proper age. They, on purpose, decide that I must have misspelled my name, and they correct it for me by moving the I after the N.
**Michele Mancioppi (Dash0 Inc.)** 04:45 Yeah, I mean, naturally, it's… of course.
**Antoine Toulme (Splunk Inc.)** 04:48 Huh.
Obviously, I can't type my name, right?
**Michele Mancioppi (Dash0 Inc.)** 04:52 Nope.
**Antoine Toulme (Splunk Inc.)** 04:52 Don't worry about it.
It's… it's not important. Okay, so… What's up, folks?
They're from working?
**Michele Mancioppi (Dash0 Inc.)** 05:07 Yeah, we are… we do not have PRs open.
I just pinged Jacob asking if there is any progress on publishing the Injector docs on the OpenTelemetry.io website.
**Antoine Toulme (Splunk Inc.)** 05:20 Okay.
**Michele Mancioppi (Dash0 Inc.)** 05:20 For the rest, I would say pretty uneventful weeks.
The injector works, and it keeps working. It's nice.
**Antoine Toulme (Splunk Inc.)** 05:32 Docs on OpenTelemetry.io… Jacob, do you know about that?
**Michele Mancioppi (Dash0 Inc.)** 05:39 I, just pinged him.
Oh. He's here.
**Jacob Aronoff** 05:41 Oh, I'm… yeah, I'm here.
**Michele Mancioppi (Dash0 Inc.)** 05:45 Excellent.
**Jacob Aronoff** 05:45 I have talks locally that I wrote, like, the weeks that I responded to that ticket, that issue, I have been going through and reviewing them, and, like, testing them to make sure that they're accurate, still. But then I got… I was on vacation, and then I was away… so I was on… I was away on vacation for, like, 10 days.
And then I got pulled into a bunch of customers' stuff this past week.
So, it's been busy. So, I'm hoping to be able to get back to that, today, tomorrow.
To have that up.
Depending on how detailed we want these docs, but…
**Michele Mancioppi (Dash0 Inc.)** 06:23 I, we have not yet published anything there, so there might be… some, additional setup needed by declaring the mapping from content to GitHub user groups. If you, look up my name in the OpenTentry.io repository, you are going to see what I had to do for the packaging SIG.
**Jacob Aronoff** 06:46 Yup.
I'll look it up right now.
Where's your… there we are.
**Antoine Toulme (Splunk Inc.)** 07:04 Cool.
**Jacob Aronoff** 07:13 Yeah, so that's… that's the main thing on my list, that I'm hoping to get out.
**Antoine Toulme (Splunk Inc.)** 07:21 So, if the injector is boring and everything works, could we just start to send signals that were stable or something like that?
**Michele Mancioppi (Dash0 Inc.)** 07:30 But Antoine, we are still not done the piece de resistance, where you explain to us why IBM cannot give us mainframes this week?
**Antoine Toulme (Splunk Inc.)** 07:39 Do you really want to go into that, dude?
That's true.
**Michele Mancioppi (Dash0 Inc.)** 07:43 I'm not gonna let… I'm not gonna let on, I mean, that thing is a pain in our backsides.
**Antoine Toulme (Splunk Inc.)** 07:47 It's… Nikola Grcevski @ Grafana / OpenTelemetry 07:48 We discussed this last week, but… I mean, why not QEMU this? I mean…
**Michele Mancioppi (Dash0 Inc.)** 07:56 Because I tried, and it broke.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:01 Because I think…
**Michele Mancioppi (Dash0 Inc.)** 08:02 Yeah, then it broke.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:04 Well, let's try again, but listen, listen. I mean, we're a user space… application, right? I mean, like, QEMU has to boot correctly 390, or, like, PowerPC Linux or something like that, there's so much going on in the OS that… that could go wrong. If we manage to get to that point.
And if IBM even gives us hardware, nothing guarantees that it'll be more stable.
I mean…
**Antoine Toulme (Splunk Inc.)** 08:30 Okay. I mean, it's a step on the way, in any case, right? That's what you're saying.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:36 Yeah, I mean, it's somewhere, and if people start reporting problems, we can revisit this, but I think an OS booting has so much more going on than we will ever encounter.
**Bastian Krol (Dash0 Inc.)** 08:47 Yeah.
Hi.
**Michele Mancioppi (Dash0 Inc.)** 08:49 Ben, what image would you use to test it on?
Because you need, you need the user land, right?
**Antoine Toulme (Splunk Inc.)** 08:57 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:58 Yeah, I mean, we test QEMU regularly in OB with different architectures. We just got, like, for a while, we didn't have ARM runners.
So we tested all of the ARM distribution.
just running on emulator, essentially, on x86.
Never had a problem.
So, what, what.
**Michele Mancioppi (Dash0 Inc.)** 09:18 What they're suggesting is… We are going to run the, S390X, run, like, image for Debian and one for Rattat.
And that is gonna catch most of the bugs, because if SIG compile is weird, or there is some funky stuff with the libc, we don't need the actual kernel to figure it out, it's all userland.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:46 No, we would run the actual 390 kernel, just… Emulate390.
Essentially. So, we'll get an IBM Linux distribution, whatever it is, for 390, From Red Hat, let's say, or Debian, and boot it. If it boots, we run the Injector test. We build, we run.
**Michele Mancioppi (Dash0 Inc.)** 10:06 I could live with that.
Yeah, well enough.
**Antoine Toulme (Splunk Inc.)** 10:11 Okay.
Sue, I'll give you… I'll give you the cliff notes.
Last time I talked about this with you all, I think I was at the point where the Linux Foundation came back and said, actually, we don't need to sign these papers, it's not on us. The maintainers should be signing that paper.
Is that right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:32 Yeah.
**Antoine Toulme (Splunk Inc.)** 10:34 This is where I sit? Okay.
To which I replied, that makes absolutely no sense. The whole reason I'm here talking to you is because the maintainers cannot sign that paper. Please go and actually do your job. So, they eventually replied to IBM with the redline version of the doc.
And the red line has some really, you know, practical, nonsensical comments.
Hey, you can't possibly ask us to accept liability for stuff in here? Like… or IBM cannot get away with these, very broad statements.
I can… I can show you the slides.
Oh, but now I'm opening Word. Yes. Okay, here we go. Let me share my screen.
So now we're having a lawyer discussion in a… significantly.
So, here you can see the LF legal counsel making some amendments and saying, okay, you cannot You know, using resources in the environment to develop, test, or report software others and open-source software is prohibited.
So… you know, Joseph Morris removed from commercial use. He said, you know, he's actually.
**Michele Mancioppi (Dash0 Inc.)** 11:49 I don't know.
**Antoine Toulme (Splunk Inc.)** 11:49 Cider,
**Michele Mancioppi (Dash0 Inc.)** 11:53 Just because having more red lines is better, right?
**Antoine Toulme (Splunk Inc.)** 11:57 Yeah, there's… I think this is really, like, this type of thing, like, CF… CLF can now… can't, as a non-profit open source foundation, take on obligations that are infinite in any given contract. There's just too much risk to the stability of so many open source projects.
Right.
So, there's… there's some pretty big red lines in here.
So, yeah, I don't know how that's going to play out, because the… It's now with, IBM.
So, I'm in the chat in between those two parties, and I'm pushing like mad every week, every other day, just trying to get them to kind of even give me an update.
Now this is with the IBM lead lawyers.
I don't know.
**Michele Mancioppi (Dash0 Inc.)** 12:48 I, I salute your heroic efforts.
**Antoine Toulme (Splunk Inc.)** 12:52 I'm not doing math except just pushing people who don't want to talk to each other, make sure they do.
Right.
**Michele Mancioppi (Dash0 Inc.)** 12:58 Maybe we should… maybe you should give a talk about this harrowing experience.
**Antoine Toulme (Splunk Inc.)** 13:03 Search… It's an entertainment photo for sure, but it's just not gonna… So, if you can get, with some QMU some validation, maybe it's better than nothing. I would say shame on IBM for making this harder than it should be.
I don't know what's going on here.
But, yeah.
**Michele Mancioppi (Dash0 Inc.)** 13:24 As you can imagine, I would be more than eager to express my very complex feelings on the matter to anybody who will listen, so… Sure. We can go ahead like that, and then blame it on Big Blue.
**Antoine Toulme (Splunk Inc.)** 13:36 You wanna… you wanna take turns to yell at them? Yeah, feel free, like, this is… I'm happy to put you in the chat, and, you know, you're gonna be able to see, like, the…
**Michele Mancioppi (Dash0 Inc.)** 13:44 No, no, I'll have a go and post it, post it on LinkedIn, and take a megaphone and scream it at the next Keepcom.
**Antoine Toulme (Splunk Inc.)** 13:51 Well… Yes, the maintainer summit could be fun.
**Michele Mancioppi (Dash0 Inc.)** 13:55 Sorry.
**Antoine Toulme (Splunk Inc.)** 13:57 That's for sure. All the other guys, it's like, this all goes all the way to the top of the Linux Foundation here, because they… they kind of try to not get into it, but, you know.
So, this is where we are. I don't know if it's going to play out or… Properly, quickly.
Anyway, yeah, QMU is a good outcome.
So… So Antoine update on screen is finitex… Let's see… You know, ease, okay, to try, wow.
Okay, so… Are you telling me if we get S390X support, we're good to go? Because some… some joker just started to add TS3 support for salaries in Collector.
Just so you know.
**Michele Mancioppi (Dash0 Inc.)** 14:56 Who, who told Brian Cantrell where is the, where is the OpenTele in GitHub?
**Antoine Toulme (Splunk Inc.)** 15:02 No, it wasn't me. I'm innocent on this one.
I would say also X is actually more interesting than Solaris, and even S390X at this point, but…
**Michele Mancioppi (Dash0 Inc.)** 15:14 Solaris is that at least let's do Luminous con.
**Antoine Toulme (Splunk Inc.)** 15:18 Here's… We're really reaching the far end as of the universe at this point.
So, is there… so… but it's… this is a good guideline for the discussion, like, so… this Injector project is getting to the point where it works.
why would it take for us to kind of declare it GA 1.0, what have you, stable.
**Michele Mancioppi (Dash0 Inc.)** 15:39 Ready?
**Antoine Toulme (Splunk Inc.)** 15:41 LMS use.
**Michele Mancioppi (Dash0 Inc.)** 15:41 I would say the moment that we can do it, my opinion is that it's already technically stable.
And, the moment that we… that I would declare it stable, the moment that… The operator and the system packages.
have it well integrated inside. System packages, it's already done.
If we add the operator with a story around the Injector that is a little bit proven in the field, that would be good enough for me.
Because my concern is not the core technology that I think is pretty solid.
My concern is with the structure of the configurations.
This is absolutely weird.
**Antoine Toulme (Splunk Inc.)** 16:23 I think that's fair. So you try to go back to declarative config a little bit here, make sure it's also used properly across the board.
**Michele Mancioppi (Dash0 Inc.)** 16:30 So that we have…
**Antoine Toulme (Splunk Inc.)** 16:31 mechanism.
**Michele Mancioppi (Dash0 Inc.)** 16:32 Yeah, so… I also, I'm not…
**Bastian Krol (Dash0 Inc.)** 16:34 we discussed this, question, how do we become stable or 1-0 before, like, in January. I just posted an issue to the chat where we, written up a couple of docklings, at least, from the specification for what are prerequisites for that?
So, if you want to discuss… I think it should be something that we should put under our… near-term future agenda, and I think we should revisit these things. Like, you raised your hand.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:12 You pointed out exactly what I was gonna say. We need to have a document somewhere describing what constitutes a breaking change, what our API contract is, what our behavior contract is that we guarantee we won't break. Just the obvious stuff, get it in writing, so that we know what we are beholden to, and which areas we have flexibility in evolving going forward.
**Michele Mancioppi (Dash0 Inc.)** 17:37 But the, the current, for example, the comments that I… that I see, they were more geared Still for the world in which the packages lived in the injector.
**Bastian Krol (Dash0 Inc.)** 17:49 Yeah.
**Antoine Toulme (Splunk Inc.)** 17:50 That's true, okay. It makes it simpler.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:53 Yeah, it's probably quite simple, but, you know, like, what is the API that you use to enter, to… to interact with the injector. There's the configuration interface, maybe the location of certain files, or that we look for things by default, any environment variables that kind of correspond to our file configuration interface.
And maybe other things as well, I'm not sure. Like, so we kind of have to do a scan of the behaviors that we have, and where we want to make… where we want to make guarantees, and where we want to leave things open.
**Michele Mancioppi (Dash0 Inc.)** 18:31 Actually, that reminds me that I have yet to open up stream the pull request for the… adding the definition of when is a language automatically injectable?
And, it's something… it's something that I could do today.
If we are all okay on blitzing it to the plus ones, so that it goes through without the same kind of silliness.
I was subject to recently for other similar things.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:58 I'll definitely review that.
I don't think… I don't think you'll, you know, I don't think you can do something like that without, like, having a discussion, so you can't blitz it.
**Michele Mancioppi (Dash0 Inc.)** 19:10 No, no, the… I don't want to skip the discussion. I want to, the whole point was to have a first internal round of things.
And then present it where we are… a whole… already a bunch of maintainers are in agreement that that is the right direction.
Because there is a certain trend that, the first person jumps on it and makes comments tends to derail merging stuff in the specs, significantly.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:42 Well, what I can say is that I'm on board with adding that to the spec, and like, you know, some recent spec work that you did, like, I'll engage on the conversations and try to make sure that they constructively resolve.
**Michele Mancioppi (Dash0 Inc.)** 19:56 Thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:59 I don't think… just… just… I don't think we should block our stability based on the stabilization of a spec document that describes what the language requirements are for injection. That's gonna be a longer road, and, you know, I think we can probably stabilize without that. At least, you know, that's the line I would draw in the sand to be proven otherwise.
**Michele Mancioppi (Dash0 Inc.)** 20:24 But he also said that we should go and make an inventory of what our contract is to word different languages.
And, I am, Not 100% convinced that us putting forward the contract without being signed by the other party, the language SIG.
**Bastian Krol (Dash0 Inc.)** 20:43 It's good enough.
**Michele Mancioppi (Dash0 Inc.)** 20:44 First ability.
**Bastian Krol (Dash0 Inc.)** 20:45 the more contracts towards who integrates the Injector through the configuration surface, like, from the operator, or from packaging that integrates the Injector, I think that would be the more interesting surface that… where we have stability guarantees.
I mean, we are… we… for now, we just are consumers of the Node.js out-transplantation, or the Ruby outransplantation. We don't provide a contract in their direction.
**Michele Mancioppi (Dash0 Inc.)** 21:18 Right? But they are, like, the Ruby out instrumentation, the Node.js out instrumentation, even the Java agent, which… the way you inject it will literally never change until the death of the universe. They're under no obligation To keep the way the data injection works, stable, yeah?
**Bastian Krol (Dash0 Inc.)** 21:40 That's correct, but that's… Still a different question from our own stability guarantees.
That's maybe stability guarantees in our dependencies that we would like to have.
But it's not directly the same question as, what Is, what does it mean that the injector is, stable, or 100?
**Michele Mancioppi (Dash0 Inc.)** 22:07 So, let me, let me try, to make a counterfactual.
let's say that tomorrow we declare stable, and the day after tomorrow, Node.js puts out the SDK 3.0, which changes entirely the way that injection has to work.
Then what you would say is the Injector doesn't change in its stability.
We will just say that it doesn't work yet with the version 3, and then we'll find somehow a way through configuration or something to implement, to activate a new behavior for the Node.js SDK version 3.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 22:49 reasonable to me.
**Bastian Krol (Dash0 Inc.)** 22:50 Yeah, the way I would see this is that we then cannot… bundle the Injector with that hypothetical new Node.js.
Package, because it doesn't work together that… Basically, it means we probably need… would need to… At least, yeah, you're right in the sense that we need to list the auto-transplantation agent versions that are proven to work with the Injector. That's probably a thing, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:19 Well, I think it depends on the shape of how this would work in this scenario. So, if this version 3 came out and was incompatible with the injector, and the only way we could make it compatible with the injector was at the expense of the version 2 compatibility, then that would be a breaking change to the injector. And, like, that would be problematic.
But if the version 3 came out, and it worked in a… it had a breaking, you know, it broke its integration with the injector.
But we could be forward compatible with it, we can involve the ejector in such a way that we could be compatible with both version 2 and version 3 without breaking version 2, then I think that's perfectly fine.
**Michele Mancioppi (Dash0 Inc.)** 24:00 Yeah, I could swing like that.
That could work.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:05 So, like, you know, from a stability guarantee, from… we want to identify the set of things, the set of contracts and behaviors for the injector, the minimal set of things that we need to convey to, you know, users of the injector in order to have a useful experience with that, and make those guarantees and know more. We want to, like, minimize the set of guarantees that we make at stability time. So that's, like, the principle there. And so, if we can get away with stabilizing without, you know, stabilizing the contract of what it means to be injectable, then we should try to do that.
**Michele Mancioppi (Dash0 Inc.)** 24:44 Then, in this case, it seems to me like… like, the one thing that is spraying, On my brain for this kind of stuff is that I really don't like our configurations.
**Antoine Toulme (Splunk Inc.)** 25:00 that might be a way for us to get into the discussion in a constructive manner, explaining that the stability of the injector requires us to have a good idea about some of the conversion aspects. Really, what I wanted to start with this conversation today was just Are you interested in making the Injector a stable project?
Is this something you want? I just want to make sure we're aligned on this before we engage, because this is a meaningful amount of work.
And it will take different aspects of it, as we discussed, and I just wanted to be sure, like, if there's anything that we're missing out.
It's a good time to be sure.
**Michele Mancioppi (Dash0 Inc.)** 25:35 I, I feel that… the optics for an adopter, I mean, the kind of… complicated logic, not to use the word dark magic that Injector does.
Of course, having something declared stable gives you more security around adopting it than otherwise.
I mean, we even see to the collector, right? It's… for all intent and purposes, it's rock solid. And still, there are people that are held back from the version numbers starting with zero dots.
**Antoine Toulme (Splunk Inc.)** 26:08 Yep.
It's not gonna get better soon.
**Bastian Krol (Dash0 Inc.)** 26:12 I think it's not only optics, I think it's the right point in time, and it's worth doing.
**Antoine Toulme (Splunk Inc.)** 26:19 Okay, okay. Sorry if this sounds like I'm forcing a really, conversation that might be… Obvious, I just want to make sure.
**Michele Mancioppi (Dash0 Inc.)** 26:29 So, do we make, do we try to gun for KubeCon to declare stable?
**Jacob Aronoff** 26:36 2 months?
**Michele Mancioppi (Dash0 Inc.)** 26:39 I mean, if, I think it, to some extent, depends on whether… We actually want to consider changing the configuration format, or we just say, it's good enough, and then, the amount of actual work, technical work, is limited, right?
**Jacob Aronoff** 27:00 It depends on how much, we would potentially break by changing the configuration, and if you wanted to accept a dual state there. Like, if you go for stability by KubeCon, you know, I don't know if… The configuration format that you want.
is going to be compatible with the previous one, which would then make it so that you'd have to push it, like, a breaking ginger immediately.
**Michele Mancioppi (Dash0 Inc.)** 27:25 I don't even have a desired end state, you know, for the configuration format. I'm just saying that the one that we have now, I don't like it very much. I feel… it doesn't feel OpenTelemetry enough, because it doesn't look anything remotely like to the declarative configuration format.
**Bastian Krol (Dash0 Inc.)** 27:40 So, I think it'.
**Jacob Aronoff** 27:42 Nice.
Yeah, I think that that should be cleaned up before we go stable. Certainly, like, we should have a better idea of extensibility, for the configuration.
If… so that we can, like, add things in the future if we needed to.
I'm worried that if we go stable with what we have now, and then we need to add stuff, resulting in a bunch of braking changes, it's just gonna be a lot of headache, like, a lot of headaches.
**Michele Mancioppi (Dash0 Inc.)** 28:08 I'm not even saying that we should adopt the declarity configuration language, because actually, from the top of my head, I don't see anything in the declarity configuration language that is directly applicable to the Injector.
But the fact that it looks so different is what gives me a little bit of pause.
**Jacob Aronoff** 28:27 Ergonomics of it.
**Michele Mancioppi (Dash0 Inc.)** 28:28 Yeah, it feels… I mean, it's not even hard to use, I mean, ultimately, it's a text file, the key value pairs, it's very Linux-y.
**Jacob Aronoff** 28:37 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 28:37 that, like, it feels like 1990s, yeah?
Does it have even a little bit of YAML?
To, to ruin your day.
**Jacob Aronoff** 28:47 Boy.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:48 I don't even know.
**Jacob Aronoff** 28:49 in there. That's the law. I mean…
**Bastian Krol (Dash0 Inc.)** 28:52 I think these questions are all somehow have impact on each other. When do we want to have it stable, and what is the scope of that… that work, and so my ideal… in my head, the ideal sequence of steps is define the a better configuration surface that we are all satisfied with, because the current one, let's be honest, it's just grown historically without much design thought and put into it. So, design, the… configuration… nicely Make Zapbreaking changes while we are still not stable?
And then go for the rest of the stability, whatever that entails, work items. And that, in my mind, means let's not commit to a specific delivery date for that.
**Michele Mancioppi (Dash0 Inc.)** 29:52 Yeah. Oh, by the way, it just came to me, something a bit horrifying. Does SIG need to hit 1.0 before we can declare a language that the injector.
**Jacob Aronoff** 30:02 SIG is not hitting 1.0 for at least 5 years, is my bet.
**Michele Mancioppi (Dash0 Inc.)** 30:08 I don't know if SIG will ever hit one, though.
**Bastian Krol (Dash0 Inc.)** 30:10 But we don't ship it, we just compile with it, so I don't think that…
**Jacob Aronoff** 30:14 Yeah.
**Bastian Krol (Dash0 Inc.)** 30:14 that event.
**Jacob Aronoff** 30:15 I agree.
**Antoine Toulme (Splunk Inc.)** 30:16 So, Bastia, I will counter just a little bit here, is that, Michele was asking if we want to do it by KubeCon, but he didn't say which KubeCon.
So…
**Jacob Aronoff** 30:31 Very sly.
**Antoine Toulme (Splunk Inc.)** 30:33 PFP for KubeCon EU is open.
Until mid-October.
We have a little bit of time between now and, let's say, two, three weeks from now, to see how we feel about this, if we could put up a talk.
from all of us here, to say, hey, we're gonna do a discussion at Couponio where we discuss, like, stability of this injector, and we'd like to make a big statement. I think that's the right idea. We could do that the way it was well thought through.
**Michele Mancioppi (Dash0 Inc.)** 31:01 I love it, and we could even put the history of the Injector, and how it came to be, and what we learned on the way.
**Jacob Aronoff** 31:07 Good.
**Antoine Toulme (Splunk Inc.)** 31:07 all those things, and then the downstream effects of it, and how this is going to help the operator, the packaging effort, how this helps the ecosystem, and SIG as well. Like, all those type of discussions that we're having in this meeting, I think could be reflected nicely with all how they impact different aspects of what we're doing.
Alright, so…
**Michele Mancioppi (Dash0 Inc.)** 31:29 I promise I will not even mention the drama of S9TX unless somebody else does first.
**Antoine Toulme (Splunk Inc.)** 31:35 I'll just use it as my laptop background when I load up the slides or something like that.
**Jacob Aronoff** 31:42 That's when…
**Antoine Toulme (Splunk Inc.)** 31:43 No, that's fine.
**Jacob Aronoff** 31:44 One… one brief thing. I… this is… I have to head out now for the operator SIG. I noticed that our SIG version's still on 15. Anybody opposed to bumping that to 16? I can do that work. I did this migration recently for, like, one of my own projects.
**Bastian Krol (Dash0 Inc.)** 32:01 That would be great. I didn't even know that there is a 16…
**Jacob Aronoff** 32:07 Yeah, 16 changes…
**Bastian Krol (Dash0 Inc.)** 32:08 We probably should, at some point, should at least have some GitHub job set that at least opens the PR when a new SIG version is out.
**Jacob Aronoff** 32:16 Oh, that's…
**Bastian Krol (Dash0 Inc.)** 32:17 But not for ZIK, yeah.
**Jacob Aronoff** 32:18 The major version changes like this have a ton of breaking changes.
**Bastian Krol (Dash0 Inc.)** 32:23 No, that's fine, I mean, I would be fine if it just opened the PR with just changing the version number, and then everything else breaks. Oh, and then it'll just break. I know that you know, okay, a new version is there, and… Yep.
**Jacob Aronoff** 32:35 Yeah.
Okay, I'll make an issue for that, and that shouldn't take me that long, versus docs. The main change is, like, a… they introduced a thing called Juicy Main, which is, it's like, rather than using the process end, you get the environment variables from the main. It's actually a nicer method, but it's… Okay.
a little bit… you have to, like, pipe them down, essentially. It's, like, a lot of drill-down, like, process arcs and stuff.
So, it's just more things to drill down in addition to I.O. now.
But, you know, it's what it is.
Let's amazing for it.
**Michele Mancioppi (Dash0 Inc.)** 33:15 I need to run. I'll put a draft of the proposal for KubeCon in the channel at some point today.
**Antoine Toulme (Splunk Inc.)** 33:24 Thank you, Nikola. Thank you all.
**Michele Mancioppi (Dash0 Inc.)** 33:26 Bye.
**Antoine Toulme (Splunk Inc.)** 33:26 Okay, bye.
**Bastian Krol (Dash0 Inc.)** 33:27 Bye, bye.
