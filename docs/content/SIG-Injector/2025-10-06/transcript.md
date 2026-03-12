SIG: SIG Injector
Date: 2025-10-06
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/EjaCCLYUiYObWuWwZmkwJIidLu-XfLi8tREq5pShPedwujlQL3D2w27ooE9qbJ9r.bg4rkP7zmDOyuGI4
============================================================

## Zoom Recording Transcript

Michele Mancioppi 00:04:05 Ed. Hi.
Tedsuo 00:04:08 Hello!
Michele Mancioppi 00:04:10 What's up? How's Ron?
Bastian Krol 00:04:12 Hello?
Tedsuo 00:04:13 Good healing, yeah.
Michele Mancioppi 00:04:15 Right.
Tedsuo 00:04:16 It's in this very weird phase right now where The nerves are starting to come back.
Which means it's like, you know that sensation when, like, your foot falls asleep or something?
It's like that, but all the time.
Bastian Krol 00:04:33 Oh, shit. That doesn't sound great.
Tedsuo 00:04:36 So, like, that's annoying, but the arm works, so that's nice.
Michele Mancioppi 00:04:42 There is always a silver lining, right?
Tedsuo 00:04:45 Yeah.
Michele Mancioppi 00:04:49 The last time we spoke, you, were, you asked us to make a, project file.
And I took a stab at it, and I'm not satisfied with what they wrote.
Tedsuo 00:05:03 Oh, I was, I was actually about to add this to the agenda. I thought a lot of what you wrote was great.
There are a couple sections I wanted to just fill in.
Real quick.
Michele Mancioppi 00:05:17 It needs, like, I was… I felt the need… I felt like… I had a feeling that I… I was not striking the right balance between info dump and scoping.
Tedsuo 00:05:27 I, I, I do have a little bit of worry about… you know, just, I want to make sure we don't accidentally re-litigate things, you know what I mean? Like, we already went through accepting this donation and stuff like that, right? But now, we're getting onto, like, bigger visions.
Michele Mancioppi 00:05:44 Around, like, package management and, like, a real install experience.
Tedsuo 00:05:49 So, that would be my one thing, is I want to make sure when we put this project file in, people do not misinterpret this as, like.
we are right now starting up this bigger effort, because that might… like, I don't want people coming in and being like, you can't work on this injector, because we didn't approve it yet.
Which wouldn't happen…
Michele Mancioppi 00:06:07 Isn't that past… isn't that way past before us?
Tedsuo 00:06:10 I think so, but because we didn't, like… do this when we should have, right? It might look to people right at this moment when we're super crunched for time and really not wanting to start big, new projects.
Michele Mancioppi 00:06:26 At the time you came in.
Tedsuo 00:06:27 starting a big new project. We… I'm saying we aren't starting a big new project. I'm just, like, let's make sure…
Michele Mancioppi 00:06:33 I want it on the record, and Zoom be my witness.
When you came in two weeks ago asking about Precify, it was the first time I heard that these things exist.
Tedsuo 00:06:43 Yeah.
Exactly.
Michele Mancioppi 00:06:45 So that's very clear.
Tedsuo 00:06:47 you're not doing anything wrong, to be super clear. This is like… like, when this donation came through, I was like, okay, so some code got donated and went through the proper thing, and then you guys started a SIG, but, like.
did anyone, like, do all the new SIG things that we're trying to do now? And it's like, didn't look like we did them. That's fine.
But normally, if we were to start a SIG up like this, we would want to figure out things, like, who's the TC member, who's the liaison for this SIG?
And how, expect, how involved are they? Are they just, like, a point of contact? So when the SIG… is, like, confused about how things work. They know which… who they can reach out to.
Or is there a TCM?
Michele Mancioppi 00:07:34 We know exactly what we want to do. It's all the same monies around it that confuse the hell out of me.
Tedsuo 00:07:40 Yeah.
Michele Mancioppi 00:07:43 How about what you want to do? We're crystal clear.
Tedsuo 00:07:46 I'm just trying to get, one, the paperwork in order, and… because I want to get more people involved in this SIG, but I'm just saying, if we… I feel your need to, like, strike a balance here, because we have, like, what this… the last time I was on the call here, we discussed how, like, this SIG really wants to focus on just building the injector.
Like, we should have a SIG that's just focused on this mechanism, As a standalone mechanism.
And then there's, like, all the extra stuff around packaging and, like, productizing open telemetry, right? And, like…
Michele Mancioppi 00:08:19 I don't think anybody has a problem with seeding.
The idea of the packaging is maintaining the packaging that I don't think the SIG is equipped to do.
Tedsuo 00:08:28 Right, right. We're not equipped to do that. We're not saying we're gonna do that right now. So let's just make sure that this project file doesn't… Look too much.
Michele Mancioppi 00:08:38 bootstrapping.
Tedsuo 00:08:40 Like, all that stuff.
Michele Mancioppi 00:08:41 Yeah, let's go through it, so that I can put it behind me, say, check, satisfy with it, let's go.
Tedsuo 00:08:46 Great.
Michele Mancioppi 00:08:49 So, bootstrapping system packaging of the open territory injector out to instrumentations.
Tedsuo 00:08:56 Yeah, I mean, I would just say OpenTelemetry injector, SIG.
Because we're just working on the mechanism, right? Is that… that correct?
Yeah.
Michele Mancioppi 00:09:06 No, I mean, we are, like, it's also software packaging, yeah, okay.
Tedsuo 00:09:10 We're gonna take this mechanism and use it to make a bunch of software packaging.
stuff.
Michele Mancioppi 00:09:14 Yeah.
It's not concerned.
Tedsuo 00:09:17 this…
Michele Mancioppi 00:09:19 Dude.
Tedsuo 00:09:20 He gives in… It's not.
Michele Mancioppi 00:09:23 What's wrong.
Tedsuo 00:09:25 Committing to doing temporary.
We're just coming to build a low-level mechanism.
Michele Mancioppi 00:09:29 Self, just, one of its… Delivery mechanisms.
Specifically, our line system access.
Make sense?
Tedsuo 00:09:46 It seems backwards, doesn't it?
like, we're saying this SIG… this is, like, the project file for this… what is this SIG currently working on? And my understanding is, I think, the opposite of what you just wrote. Like, we're only working on the injectors.
Michele Mancioppi 00:10:02 Okay, wait, wait a second, sir. Again, I am profoundly confused by this.
The project file is about the entire SIG, because I asked you to say, Ted, is it about the injector, is it about the system package in Scoop to KubeCon? And you said the latter.
Tedsuo 00:10:16 What, what is, what is this… yeah, so this SIG is working on building the injector. We have some deliverables we want to aim for, for this SIG.
you know, starting with KubeCon, we have, like, a couple of phases we want to go through.
But my understanding from the last call was people were saying, like, there's more… work that needs to be done to turn this into a product, then… build out this injector in stages, right? You need to then take it and… use it in all these different package management systems and places, and this SIG is saying, like, we're not… Except as maybe some kind of proof of concept, we're not… we're not doing that.
Michele Mancioppi 00:10:59 Hence.
Tedsuo 00:11:00 So that's… that's the main thing, is like… like, to… to say that… just to mention, like, we're only working on the injector. So when you say, this project file does not concern the injector itself, that seems confusing.
Michele Mancioppi 00:11:14 Now, the project file… Is it the scope is the entire SIG, or is it just the one initiative we have into KubeCon?
That is the part that I've heard both versions.
Tedsuo 00:11:28 So, it's… it's… you want to put in as much as you can till when we say this SIG is then going to… to re-up. Like, if you want to say the SIG plans on having a couple of stages.
That's okay. I don't want to focus on, like, dot dot dot, and then we're gonna do some cool stuff later. Let's just be clear about what this SIG is trying to deliver now until KubeCon, and then, like, we can talk a bit about what this SIG plans to do after that.
But in addition to what this SIG may want to do after that, my understanding was people wanted a separate SIG to get formed, that was separate from this SIG to do the packaging and the productizing.
Because that might be a different mix of people.
Now, maybe you have a different opinion of that. That was… I think I was hearing that maybe more from Bastion.
And other people.
So.
Michele Mancioppi 00:12:26 No, I can go down both ways. I just, I said, okay, I'll give it a stab, because that is usually the way that I clarify my confusion, and I was somewhat confused from the last time we spoke.
Tedsuo 00:12:37 Yeah.
Michele Mancioppi 00:12:38 Okay, let's see…
Tedsuo 00:12:40 Don't… don't let me confuse you too much. I… I think this is a good… What you wrote is generally good.
What's your concept of… The deliverables, like, every… all the details you put in seem fine to me.
About what we intend to deliver.
Michele Mancioppi 00:13:03 packages… We do not foresee this segment.
to maintain.
It's system, practices beyond… The, scope of a proof of concept.
But rather to involve… Other SIGs.
Potentially.
With, hope, of… finding… Oh, God.
Tedsuo 00:13:36 Yeah.
Michele Mancioppi 00:13:37 I can… I can do a pass on some of this and clean it up.
Tedsuo 00:13:41 Don't, don't worry too much.
Michele Mancioppi 00:13:43 Oh, this part is fine.
Tedsuo 00:13:45 That seemed fine. The challenges seemed like a good description.
you know.
Michele Mancioppi 00:13:59 Yes, then, since it's not only about the packaging, then we should also address the operator.
We kind of… we do.
Tedsuo 00:14:10 That's actually a question, right? Are we gonna be working on the operator in this SIG? Are we going to have the operator make use of this injector?
Michele Mancioppi 00:14:17 I think that some of the participants in this SIG, may engage the operator SIG.
Tedsuo 00:14:23 Yeah. To actually see it. If anything, this SIG is actually an offshoot of…
Michele Mancioppi 00:14:29 Some people in this room meeting each other after going and aggressively accosting the operator seat to say, hey, let's do all the preload, hey.
Bastian Krol 00:14:38 Maybe in the same way as you wrote about the system packages, like bootstrapping that, but not forever maintaining the integration point.
Michele Mancioppi 00:14:46 Exactly.
Tedsuo 00:14:47 Yeah, yeah, I think that's… that's a nice thing to say, is like, we're gonna build this, and then we're gonna go back to the operator SIG.
To integrate it with the operator.
Michele Mancioppi 00:14:58 We foresee as part of the SIG.
a collaboration with the equipment telemetry operator, SIG.
To, deliver the interactor.
Cool. 8.
operator, and… Short doing… Streamline.
Auto.
Strong rotation.
Experience.
I'll say not to affect… interactive seed.
Actually, it was hardened.
Spun.
Okay.
So, this effectively says, the operator people, no backsis.
This, I think we can remove, because the other one… Is, less detailed and… generally fine.
The ghosts were missing bits.
Provide, copy.
Van mouse?
Profile.
growth of this.
Do we capitalize proof of concept around here?
Antoine Toulme 00:17:04 Sure enough.
Tedsuo 00:17:05 Sure.
Michele Mancioppi 00:17:11 system, like, proposal.
No, we actually had… there, done.
Oh, good enough.
You're not?
The word operator is very overloaded.
Tedsuo 00:18:09 True. It's true.
Michele Mancioppi 00:18:10 just practitioners.
Tedsuo 00:18:13 So… Yeah, I've been… I've been trying to work on my pitch. I'm actually gonna give a… a rough version of this pitch. I'm in London at, OBSCON right now, and I'm gonna do a talk on Wednesday, Here, that's just, just, like, broadly speaking, showing, like.
what we can install easily now, and, like, what we're working towards installing in the future. But one of the angles I've noticed is, like, all of the work we're putting in right now, everyone's like, we need better docks, we need better docks, we need better docks.
But with…
Michele Mancioppi 00:18:48 It's boring, right? We could just make something that works on the internet.
Tedsuo 00:18:51 And, like, if you make better… the bigger problem is application developers can use the docs to install SDKs and instrumentation. But if you're, like, an SRE or an operator, whatever we want to call a sysadmin these days.
Like, those docs are useless, because you don't have access to that stuff, generally speaking.
Right, and it's also very slow going, right? Because you have to go.
Michele Mancioppi 00:19:18 application, whatever. I know.
Tedsuo 00:19:20 at a time.
Michele Mancioppi 00:19:20 I used to refer this in my internal days as the span of control.
Tedsuo 00:19:25 Yeah.
Michele Mancioppi 00:19:26 It's also a bit of a tragedy of the commons, because the people that need observability cannot procure themselves observability, and people that can procure the observability by modifying software, they often do not care about the externalities of not having observability.
Yeah. So there is always that social-technical tension inside companies where the operator doesn't know what's going on, but the developer says, sorry, I need to add another button.
Come back next.
Quarter.
Tedsuo 00:19:52 Right.
Who… can people just directly solve their own problems, or do they have to go through people who are busy and don't care?
Michele Mancioppi 00:20:01 That was the entire, the entire claim to glory of Instana. He would just install the agent, and it would do a lot of terrible things, and you would… you wouldn't.
Tedsuo 00:20:10 Exactly.
Michele Mancioppi 00:20:10 It was not to compare.
Tedsuo 00:20:11 That's… that's the thing we're saying, and this is… I wanna… when we start proselytizing about this to the larger community, we're gonna get some pushback from people who are like, we should just make the dogs better, we…
Antoine Toulme 00:20:24 Auto instrumentation.
Michele Mancioppi 00:20:26 And then we look at those people straight in the eye and say, great idea, go and do that, meanwhile we do this.
Tedsuo 00:20:32 Right. Well, No. We're gonna… we're gonna pull the community along with us, right? We're not gonna… we're not going to be.
Michele Mancioppi 00:20:41 No, people that come and say, oh, go and do better instrumentation.
Documentation said, nope.
Tedsuo 00:20:47 But… but… so this is the case I want to make to people, is there's… there's two different audiences, right, that have main audiences that have access to different things, right? There's…
Michele Mancioppi 00:20:58 Beautiful.
Tedsuo 00:20:58 whatever word… I've been using operators a lot to essentially say sysadmins.
Because they don't like being called cisonyms anymore for some reason.
Michele Mancioppi 00:21:09 It's up.
Antoine Toulme 00:21:09 That's not how they get… they can't get the next job if they have CSME in the title.
Tedsuo 00:21:13 I know, I know, the same way you can't be an application, you gotta be a full-stack engineer or some bullshit. Yeah, of course. Whatever. You know, why can't I just… it's still just fucking Perl scripts.
But…
Antoine Toulme 00:21:25 I mean, you know, this admin rhymes with PHP in my admin, so…
Tedsuo 00:21:30 Yeah, it's all still LAMP stack, if you look at it sideways. But, the bigger point is that, like, we want to say we've got operators and we've got developers.
Right? They have different needs, they have access to different things. Like you were saying, people need to be able to get their job done directly, and the reason why we need the injector is there's a whole bunch of stuff that operators just literally cannot install right now.
There's a couple of things they can install, and that's what's kind of in the oper… The open telemetry operator already, right? Like, our digital operator can install a couple of things, but it… that's it, right? And the reason it doesn't install the other things is, like, there's no mechanism for it to be able to do that.
And that's why we need to build this, is there's a whole audience out there, and there are many, many organizations where that's actually the person Who's gonna be the person who does this?
Antoine Toulme 00:22:27 So, so, Ted, who's going to be the people who are going to have the bandwidth and, Frankly, the wind in the lungs to go and complain about the fact that this exists.
Tedsuo 00:22:37 You know, it's not about people complaining about stuff existing, it's just about the fact that OpenTelemetry's, like, stretched pretty thin. So we're really trying to increase our project management and, like.
decrease the number of initiatives, because we… OpenTelemetry has this, like.
Antoine Toulme 00:22:59 We live in that one, huh.
Tedsuo 00:23:00 slow. We feel like we're slow, and when we've looked at it, it's that we have, like, there's, like, hotel max threads.
Antoine Toulme 00:23:07 And MaxThreads is, like…
Tedsuo 00:23:10 you know, TC members times two, roughly, and we have, like, many more projects than that. And as a result.
We've got, like, people, like, context switching between lots of different things, and that's making everything slow.
Michele Mancioppi 00:23:24 To be perfectly honest, there is no amount of slack that will make people write coherent documentation at scale.
Tedsuo 00:23:31 Right, what we need is more focus, and in order to get more focus, we need to be doing fewer things in parallel, and then we will be shipping those individual things faster and better.
And if you have, like.
If you've… just like with a computer, if you've just totally… oversaturated your CPU cores.
Everything is gonna get done, but everything is gonna get done slower.
Antoine Toulme 00:23:59 No, but, you know, no, no, wait, wait, wait, wait. There's many, many, many, many, many things you're saying here which are interesting on their own.
One of them is first that we are going to limit the capacity of the project to the capacity of the TC, which… I don't care for, I'm sorry, get more people in your TC, right?
Tedsuo 00:24:14 Absolutely. Well, we're doing some changes there, too. We're gonna have a bunch of spec maintainers, so we're trying to take a bunch of TC responsibility and say, here's all the spec maintainers. So we're trying to find ways to get more people.
Antoine Toulme 00:24:26 Delegate. Delegate, right.
Tedsuo 00:24:28 But here's the problem, Anthony, is we've noticed that when SIGs just work off in a corner, right, and they don't… could, like… If the work they're doing is generally work that could stay off in a corner and no one would ever have to care about it, then great. But, like, for SIGs.
more often than not, when the SIGs go off in a corner and work for a long time, and then come back to the community and be like, we built all this shit without anyone giving us any feedback.
Like, that often doesn't, like… result in success.
Because these things are too interrelated with each other, so we want to make sure that we aren't doing, like, experimental projects, and I don't want to waste your meeting talking about this, by the way, so I'm going to shut up after this. But, like, we don't.
Bastian Krol 00:25:14 I think this is extremely important to get this straight, so take the time.
Tedsuo 00:25:20 It's… we… we just recognize that, like, we can't keep spinning up more and more things, right? And what keeps happening is more and more people are interested in OpenTelemetry, so they want to do more. And we want to keep saying yes, so we do, but if… if it's totally diffuse.
and there's no organizing across the little fiefdoms, then the project loses coherence. And OpenTelemetry right now, to me, already feels like it's like, I want the injector as part of this process of bringing some coherence back.
Right? You know, we have, like, lots of pieces now, there's lots of things that need to get targeted with those pieces. The community needs to know, like, what is all this, like, giant pile of stuff I have to install, right?
Antoine Toulme 00:26:09 Oh, okay, okay, so…
Tedsuo 00:26:11 It's, it's like…
Antoine Toulme 00:26:11 That's weird.
Tedsuo 00:26:12 People are really feeling like we're hitting a wall here, where we need to, like, stop adding new shit, and just go to town, like… Mac, do you remember Snow Leopard?
when…
Antoine Toulme 00:26:24 Yeah, yeah.
Tedsuo 00:26:25 Finally, it was just like, you know what, we're gonna just, like, make things not suck for, like, a year, and not keep adding new crazy shit.
Antoine Toulme 00:26:32 So, okay, so…
Tedsuo 00:26:33 What we're doing… here, and this is my final point. What we're doing here is critical to that effort, in my opinion.
Michele Mancioppi 00:26:40 It's also crazy shit, but a good kind of crazy.
Bastian Krol 00:26:43 Yeah, but, I mean, is there…
Tedsuo 00:26:45 Do you see why we're gonna run into a wall, right? Because we're trying to solve people's problems, but we look like we're trying to do the opposite.
Bastian Krol 00:26:54 Yeah.
Michele Mancioppi 00:26:55 Yeah, I get it.
Bastian Krol 00:26:55 I think we need to ask ourselves if we are actually in… run that risk of, okay, there are all these components, and we fix it by adding one more component, and now we have one N plus 1 component, and does it…
Michele Mancioppi 00:27:11 Although, to be fair, this component is the one with the highest chance of actually fixing the experience than anything else I've seen.
Tedsuo 00:27:16 This is actually the thing we need more than anything, in my opinion, to solve a bunch of problems for the OpenTelemetry installation experience, because people keep complaining about it, and part of it is the docs could be better, but most of it is installing this stuff by hand is crazy.
We talk about it like, oh, you just, like, install some packages, right? That is not what you are doing, right? You have to figure out which packages in your app match which, like, instrumentation packages are available.
Your dependency manager's not gonna tell you that, like, nothing's gonna tell you that.
except some weird-ass, like, tools, maybe in Python or some other languages, like, every.
Michele Mancioppi 00:28:02 Python is the worst offender that I've mentioned in terms of packaging.
Tedsuo 00:28:06 Exactly, right? Everything is, like, kind of bespoke, and that's what's actually making it So if we can instead replace all of that shit with something very uniform.
Which is what this injector does.
Antoine Toulme 00:28:19 So, Ted, okay, so I took it the wrong way. I thought… I assumed that what you meant is, like, oh, the injector is just one more, distraction from the goal of open symmetry, and actually, you're saying, no, this is actually great, because it ties the boat together, and it makes it real critical.
Tedsuo 00:28:32 Right, right. But… but… but we are… but we need it desperately, right? We're trying to, like, bring the project in and just focus on, like.
getting it really, really product-worthy and productionized and easy to install. And so you're gonna have people who don't understand the APM market.
And thus, don't understand, like, why this is really necessary.
Antoine Toulme 00:28:57 Okay.
Tedsuo 00:28:58 If you're… if you're in the infrastructure monitoring market.
you kind of… you're just like… like, I don't know, you're not… or if you're just, like, application devs, like, you're… you don't work for, like, an APM company, right? You're, like, an Apple.
Antoine Toulme 00:29:13 KG.
Tedsuo 00:29:14 who works at, like, Google or Microsoft or something. You might be like, I don't… there's other factions in OTEL who might not understand how this is really solving it for people.
That's… that's the thing, right? So we need to make… and we can't just be like, shut the fuck up, right? Like, we have to sell. We have to… we want the community to be, like, happy if we're gonna come in in this moment and be like, we got… we have the solution for the problems, and we want to pivot this community towards… more of… Okay.
product, packaging-focused, kind of experience.
Antoine Toulme 00:29:51 So, so…
Tedsuo 00:29:52 We have to actually sell the community on it, because not… there's a percentage of the community that's like, obviously this is important, but there's actually a big chunk of it who doesn't have background to understand this, because they personally don't need it.
Michele Mancioppi 00:30:07 Is that true?
Antoine Toulme 00:30:08 Over here.
Michele Mancioppi 00:30:08 surprises me.
the amount of, people in the open territory community that Do not sympathize with Joe Rondo out there.
I don't get it.
Tedsuo 00:30:21 It depends on which rando. They really sympathize with the application developers, which is why they really want to, like, improve the documentation in the OTEL demo.
Michele Mancioppi 00:30:30 Vision developers don't want to add packages either manually.
Tedsuo 00:30:33 They don't want to do that, I know! They don't want it either. You know what I'm saying? It's not that people don't have sympathy, it's like… like, some of us have been doing this for a really fucking long time, and other people have not, and… and we… we need to have sympathy for those Joe Randos.
Right? Like, leadership is us selling the community on this vision and, like, convincing them. We want to be, like, in that space, not in the space of, like, bitching and complaining and demanding, right?
Does that make sense?
Antoine Toulme 00:31:03 Yeah, but I mean, I think you're trying to do parameter optimization a little bit here, because I haven't heard anyone complain yet.
And I'm very much a man who only can take it 5 minutes at a time.
Michele Mancioppi 00:31:15 Wait until the BPF people get rid of this.
Tedsuo 00:31:17 But here's the thing, we need stuff from other SIGs, right? Like, I'm hearing you guys, like, bitch about Python, right? Like, we need the Python SIG to, like, do some stuff.
Antoine Toulme 00:31:26 Oh, yeah.
Michele Mancioppi 00:31:27 No, no, no, I don't bitch about the Python's thing. I bitch about Python, the language, and the package managers. It's a very different thing.
Tedsuo 00:31:33 And, like, I'm just saying… From my perspective, there's, like, a bigger pivot around getting the whole community to focus on productizing this thing, in general.
Antoine Toulme 00:31:43 I thought…
Tedsuo 00:31:45 Can we pivot to that, have it not turn into, like, a giant shouting match, where people are all feeling a different part of the elephant? So I just want to go into that initiative with a big pitch and a plan and stuff, like, already in place, you know, so that we're not being, like.
hey, what do you all think? We're going in and being like, here's how we're gonna solve this, right? Here's… here's the product department coming in with our pitch, here's how we're gonna solve these problems, here's what the requirements are, here's what the problems really are, like, here's how.
Antoine Toulme 00:32:15 For sure you're gonna get some shit for that. I mean, you're gonna get some shit for that than if you just screw up with yourself.
Tedsuo 00:32:20 But it's gonna take a bit of work, and that's what I'm here for. I'm here to do that.
Antoine Toulme 00:32:24 Yeah, you can evangelize the vision of the.
Tedsuo 00:32:27 Happy to go.
Antoine Toulme 00:32:28 to every language, so you can have a little pitch and say, hey, please, hear me out, this is where, how we're going to politicize your shit. It's gonna be great, people are gonna love this. That's not a problem. What I would want is to avoid the bazaar versus the cathedral approach, where we try to get this right here, and we do a really good job, and then we bring it to the others, and they're like, you know what? Actually.
No.
And so… Yeah, I want…
Tedsuo 00:32:51 And the people.
Antoine Toulme 00:32:51 People bought in on the concept, yeah. But the only thing that buys people in is users.
Like, I want to download… I want to see download numbers in the hundreds of thousands, and then we'll have a talk, right? That's… to me, that's the only thing that matters.
Tedsuo 00:33:05 I mean, I mean, but we, we also know, we don't have users, because we don't fucking have this thing, right? So there's a…
Antoine Toulme 00:33:14 Well, then let's ship, let's ship it, that's fine, it's easy, let's just ship it.
Tedsuo 00:33:17 Yes, yes, we need a tip. We need a tip.
Antoine Toulme 00:33:20 It's the progressive.
Tedsuo 00:33:21 All of this is progressive.
Running song?
Antoine Toulme 00:33:25 Software solves every problem, right? Like, that's the only thing that matters. The general pivot we're making in hotel is…
Tedsuo 00:33:33 to keep rapidly, like, we don't want to slow down with this injector. We want to keep moving fast and shipping.
Antoine Toulme 00:33:39 Yeah.
Tedsuo 00:33:40 You're totally right.
Antoine Toulme 00:33:40 that's…
Tedsuo 00:33:41 We don't want anyone to block us from shipping it, and we're lucky there, because we've got enough languages that we don't need a lot of work out of that we can chip for, right? A couple of things, like.
Michele Mancioppi 00:33:53 That is enough to deliver value.
Tedsuo 00:33:54 Great in Python.
Antoine Toulme 00:33:55 Yeah, but…
Michele Mancioppi 00:33:56 There are enough to deliver value, and luckily there are some with the biggest I mean, Python would be great.
Python's probably the last to get on board of the language that can be done.
Tedsuo 00:34:07 But you can come after Python after you've shown the value elsewhere.
Michele Mancioppi 00:34:12 I…
Antoine Toulme 00:34:12 Yeah, yeah.
Michele Mancioppi 00:34:13 I know this enough.
Tedsuo 00:34:15 Totally. Yeah.
But I just… I am thinking a couple of steps ahead, just because I'm like, man, it's a big community, so, like, I gotta figure out my pitch with you guys, and then…
Antoine Toulme 00:34:29 Absolutely.
Tedsuo 00:34:30 Sell the GC, sell the TC, start selling the maintainers, and just… just beat a drum. It's not like a one giant thing is ever gonna happen, but it's like you… You just start door knocking, right? You start beating that drum.
Antoine Toulme 00:34:44 Yeah, yeah, you're… this is really important, what you're doing, Ted. I think this is… actually, I was very excited because I heard that you might be getting lunch with Jason Plum, who's a maintainer of Java.
And I was telling Jason, hey, you need to take time with Ted, you gotta talk about the injector follow our burger, because you're gonna have a lot of feedback for him in the messaging, how to present that, how to feed that to Java people.
Because there's a fine line, there's a few keywords you can say in the right order for a Java person to be like, oh, okay, sure, no problem, right?
Michele Mancioppi 00:35:15 The general people are the least… are the least people that need to be concerned about this, because their delivery mechanism is already perfect for the injector. There's nothing…
Antoine Toulme 00:35:25 That's why I'd like to start with the easy case. We get the easy wins out. You show a very nice integration, a demo. Everybody from Gelastic is, like, up on the scenes, like, yeah, great! And then one of the different guys on the back of the room is like, shit, we better get on the bandwagon.
Which is the whole logic of it.
Tedsuo 00:35:43 But can't the operator already inject the agent for that very reason?
Michele Mancioppi 00:35:46 Yeah, but it requires you to go and, exactly, that's why I said it works very well. But you still need to go and annotate the single pod, so… Effectively, there is, right?
Booking contract there.
Tedsuo 00:35:57 Yeah.
But I…
Antoine Toulme 00:35:59 And it's maintained by the operator SIG in a way that does not feel very viable or maintainable long-term.
It's in spite of itself.
Tedsuo 00:36:08 Right, right. No, the injector's great, it's just, for me, I feel like the bigger wins are the not-Javas, you know what I mean.
Antoine Toulme 00:36:15 Oh, come on, get stuck somewhere, right? I mean…
Tedsuo 00:36:17 You gotta start somewhere.
But it's… it's more impressive when you can do the… it's more… I think it's more impressive, people, when you do this with something like Node.js.
Where people are like.
Antoine Toulme 00:36:28 Oh my god. I'm not sure who did that.
Tedsuo 00:36:29 You know what I mean? Like, everyone's like, I know how you did it with Java, there's a fucking Java agent, but actually, like, what is this insane stack of stuff from top to bottom that allows us to hook in to JavaScript like this, you know?
That… that looks… feels a little more magical to people, and it's also solving a bigger problem, because they don't have a fucking Java agent in Node.js.
Michele Mancioppi 00:36:52 Can we get, by the end of this meeting, to sign off on the document?
That would be great.
Antoine Toulme 00:36:59 I…
Tedsuo 00:37:01 I like what you're… you're… writing.
So yeah, let's keep going.
Michele Mancioppi 00:37:12 I mean, please proofread the goals so that we're on the same page with the scope.
I'm always, like, I found, like, goals and milestones, it all… it's all the same thing for me.
What goals are we missing here, Scott?
Tedsuo 00:37:50 I think these… these goals are fine.
I think the goals section is… you know, I think the main thing maybe there is to… Yeah, I mean, if we wanted to just one-line it, it's like… Create, mechanism, or… .
Michele Mancioppi 00:38:25 Out of the box instrumentation.
Tedsuo 00:38:27 as… Well… as well as… to install… The SDK and… Library Instrument… mentation in…
Michele Mancioppi 00:38:53 as many…
Tedsuo 00:38:55 languages as possible.
Using… The same mechanism?
Michele Mancioppi 00:39:02 Yes, let me refine it a bit. Install, SDKs, and… Library art instrumentations applicable to All applications on a line-axis host.
Just… By means of adding… Is it urgent… There's our system packages.
And… Support as many languages.
as possible.
Wow.
Tedsuo 00:39:56 AMP.
We know from industry experience That this significantly improves installation… It says at… scale.
Michele Mancioppi 00:40:20 Yep.
Very nice.
Tedsuo 00:40:26 Especially… In situations when application… Developers are not… Something like that.
Application owners is, like, the other weird term in typical, but I don't know.
Michele Mancioppi 00:40:49 effort.
To, maintain… Observerated table set types.
Sorry.
Tedsuo 00:41:01 their applications. Yeah.
Inside all of the applications makers.
Anyways, whatever. That's fine.
So that's great, and then the rest of this makes sense, because, yeah, in pursuit of this vision.
This is how we're gonna do it.
Michele Mancioppi 00:41:20 Yep.
Tedsuo 00:41:21 Establish proposal, Yeah.
Michele Mancioppi 00:41:54 Good.
Tedsuo 00:41:56 Maybe skip.
Yeah.
Okay, so… So now we're… we're starting to repeat ourselves.
Why now?
Michele Mancioppi 00:42:13 I actually would just leave this… this was the original paragraph.
Like, we feel OpenTel Entry needs to provide more product, like, that there's including experience to newcomers.
Tedsuo 00:42:23 Yeah, there's use to the ease of… yes, and I think that's the cool key… This is especially critical when or organizations… that want… the… and again, I don't know… I don't want to use the term sysadmin or SRE, but it's, like, the system operator, or something?
want… to… I mean, I don't know quite how you… like, there's… many organizations have… it's like, we want the lowest… it's, like, almost like IT, you know? It's, like, more like the people… you're saying, hey, install this thing that can do all this, like, crazy, dangerous stuff, and basically looks like a fucking injection attack.
And organizations look… agents like that, and they're like, we want the, like.
sysadmin security person to be in charge of this fucking thing, right? Because this thing can do too many dangerous things, especially, like, after SolarWinds, right?
Michele Mancioppi 00:43:38 So instead of saying what they want, let's say what the situation is.
Tedsuo 00:43:42 Yeah.
We're operating and maintaining observability setups.
Yeah, that's perfect. That's fucking perfect.
Michele Mancioppi 00:43:56 Alright.
Tedsuo 00:43:57 Getting, library-level telemetry. Yeah.
Okay, great. So, requirements…
Michele Mancioppi 00:44:14 Okay, benefits?
Tedsuo 00:44:21 The most straightforward getting… Yeah, the benefits is… yeah.
Hmm…
Michele Mancioppi 00:44:30 Maybe we, we toot the same, the same horn.
Is this?
Tedsuo 00:44:36 Yeah.
I think it's okay to kind of repeat.
Michele Mancioppi 00:44:41 yourself here. Yep, this.
We'll enable.
Operators… That are in charge of enthusiung.
Name, oh… Operators.
The grief, the benefits of application of Library, author.
It's one dishes.
And this will front-load, because I'm not writing in Italian.
Oh, unco… Alright.
Okay. This is the same as the goals?
Just in purple?
Such a good deal.
Tedsuo 00:45:43 caffeine!
Michele Mancioppi 00:45:46 I did try to get my former friends economically involved, but… It takes an act of God for them to do something.
Tedsuo 00:45:54 I think the, you know, the one question we'll probably get asked here is about more, like, maybe, like, I mean, you can imagine people being like, why is Dynatrace not involved?
Right, they're heavily involved in OpenTelemetry.
Michele Mancioppi 00:46:08 They also have some of the best… of LD preload technologies, and that's exactly why they're not going to contribute to this.
Tedsuo 00:46:16 But have we actually asked them?
Michele Mancioppi 00:46:20 That's a fair question.
Antoine Toulme 00:46:24 We certainly have.
Michele Mancioppi 00:46:25 The answer is no.
Antoine Toulme 00:46:25 vendors.
No, we are not asking vendors proactively about stuff.
And frankly, when we have a donation thread and a proposal in a community, this is the time for vendors to chime in. If they do not chime in, the donation may proceed with whoever is interested.
Otherwise, and you can say, nope, and then that doesn't happen.
Tedsuo 00:46:46 This was…
Antoine Toulme 00:46:47 that.
Tedsuo 00:46:48 This is already signed up. I'm not saying, like, you know, for anything like that, but I'm actually curious… I mean, I actually… I guess what I'm.
Antoine Toulme 00:46:56 I know, I know.
Tedsuo 00:46:56 You should actually ask Dynatrace, because the answer might surprise us, you never know.
They'll look at this and be like, yeah, the writing's on the wall, like, screw it.
Michele Mancioppi 00:47:06 To be perfectly honest, the technology that we're working on right now, Essentially, ahead of the traces.
Tedsuo 00:47:13 They might look at this and be like.
you know, it's annoying to us that people can't install OTEL easier, you know?
Antoine Toulme 00:47:21 Yeah, yeah, that's fine.
Tedsuo 00:47:22 when you're.
Antoine Toulme 00:47:22 Yup.
Tedsuo 00:47:24 They, they might, they might be interested.
Antoine Toulme 00:47:26 Usually the answer I've gotten from people who are product managers, who are deep inside vendors, beside me, Kelly, and myself, is that they don't actually know what a transformative does, they don't go into discussions with the community, they don't really pay attention, and the last ones to pick up on any of this.
And usually, they reluctantly will look at any issue, not because we tell them to, but because the customer is yelling in their ears for, like.
You know, enough for them to pay attention.
Michele Mancioppi 00:47:51 I actually have a theory, and the theory is, if the product managers Of some of the major vendors understood.
the social potential of OpenTelemetry would never have happened.
Antoine Toulme 00:48:05 Well, this is why I'm here, right? I mean… Just be clear.
Michele Mancioppi 00:48:08 I don't know what to say. You can pick the top right corner of the quadrant.
And then go and ask to the project leader, say, are you happy about OpenTelemetry? And they will go like, yeah, of course we are.
Anything they're not.
Because it actually chips away at the most valuable asset of, I'm sorry, with the company, the vendor lock-in.
Tedsuo 00:48:34 Well, if you have faith in your product, Then, frictionless telemetry doesn't necessarily sound bad.
Antoine Toulme 00:48:44 No, it's a great idea.
M…
Tedsuo 00:48:47 But if you already… it's more that if you already have a thing that's really advanced, why do you want to, like, rebuild it from scratch? That's more what we see. If someone's already done all the work to build this Dynatrace 1 agent thing, they're like, we got one and it works right now, and we're not… So, same thing, like, with, like, browser stuff. We're like… you know, the people like Sentry and whatever, who are, like, really, really advanced, you know, they throw shade at OTEL, but also, like, we would have to get really far along on the browser before we started getting even close to, like.
this stuff they ship. So, you know, they're probably not going to be like, why… why would we be wast… it would be a waste of effort at this juncture to get involved. But later, they tend to get… those kinds of organizations get involved, once it starts to get closer to where.
Antoine Toulme 00:49:33 That's…
Tedsuo 00:49:34 Proprietary stuff was.
Antoine Toulme 00:49:35 That's half my conversations these days, right? I just had a conversation with another vendor PM, and I told him, there are two options, right? You can treat this as an opportunity or as a risk.
Which one would you like? You can put 6 months of work into making this a real opportunity where you have a leg up on the market, and you can direct the direction of where things are going. Or, you can wait, and then you're gonna have 6 months of technical debt to get back into where things should be, and you'll be at the disadvantage of the market, and people will make fun of you.
You choose, whichever you want is a valid option, depending on your options, the resources you have, the bandwidth you have, the ability to talk to strangers on Zoom calls, or whatever, but you're gonna pick one.
Tedsuo 00:50:16 And one will be chosen for you by default, if you don't pay attention.
Yeah, yeah, that's… that's very true.
Antoine Toulme 00:50:24 That's the only thing that I have to say to them. And I keep saying it until the end of times, that would be my motto.
Alright. So…
Tedsuo 00:50:33 Let's go.
Michele Mancioppi 00:50:33 Customership.
Tedsuo 00:50:34 at 10.
Michele Mancioppi 00:50:34 The name of the seed sponsor, Ted Young.
Tedsuo 00:50:37 I'm not on the TC.
Michele Mancioppi 00:50:39 Who's on the TC?
Tedsuo 00:50:40 I don't know that we have one right now, but I would like to ask Jack Berg.
Michele Mancioppi 00:50:45 That was the due diligence, right?
Tedsuo 00:50:48 Yeah, he did the due diligence.
Then… And for other reasons, I think he would be a good pick. So I'm gonna ask him, don't put anything in the.
Michele Mancioppi 00:50:56 Alright.
Tedsuo 00:50:56 Yet?
Antoine Toulme 00:50:58 GC is, Morgan…
Tedsuo 00:51:00 GC liaison, it can be me, it can be Morgan.
Antoine Toulme 00:51:04 Yeah, we can put that, so…
Tedsuo 00:51:08 I am excited for Morgan to be back in action.
Antoine Toulme 00:51:14 It's… Yeah, no, I… I depend on this man, like… the air breathe, so… Yeah, he's…
Tedsuo 00:51:24 Okay. And then we have timeline. Actually, the one thing… It is just the… for staffing.
It is just injector approvers, right, essentially?
There aren't… there aren't other engineers floating around working on other things.
We can just point it.
Michele Mancioppi 00:51:48 There are people trying to give us more work.
Tedsuo 00:51:51 Yeah.
Michele Mancioppi 00:51:54 Yeah, no.
Antoine Toulme 00:51:55 It never worked for me. You can open as many issues as you want.
Feel free.
I don't…
Michele Mancioppi 00:52:02 I mean, technically, it might be that Elastic actually brings, some help for the Python SDK to remove one of the biggest issues, that is the…
Antoine Toulme 00:52:11 Sure.
Michele Mancioppi 00:52:12 I'm looking forward to see them, lift their tissue.
Antoine Toulme 00:52:17 Let's support Ruby first, just to spite them.
I'm a small man.
No. Wait to take the higher ground, Antoine.
Tedsuo 00:52:30 Yeah, you know, the other Sigs are gonna start listening to these calls, and then they're gonna…
Antoine Toulme 00:52:33 Oh, no!
Tedsuo 00:52:35 They're crazy.
Antoine Toulme 00:52:36 Show up?
Will they give me my face? Will they maybe participate in discussions and tell me I'm wrong? Oh my god, oh, please don't come here, no!
What are you gonna do?
Michele Mancioppi 00:52:47 They may not come here with ecstatic collaboration in mind.
Antoine Toulme 00:52:51 Someone's at the door.
Tedsuo 00:52:54 Alright.
Antoine Toulme 00:52:57 It's all fun and games.
I'm sorry.
Tedsuo 00:53:00 Just making my job harder, it's no big deal.
Michele Mancioppi 00:53:04 This we already have, right?
Tedsuo 00:53:09 Okay. SIG meetings, roadmap, so this, this shit is, is just, we can just plug this stuff…
Antoine Toulme 00:53:19 I mean.
Tedsuo 00:53:21 gitHub project, this is actually… Sorry, I put this in the wrong spot. This is… Should be… under here… It's just, like… Oh… It's here.
Sig meeting is… Do we have this on the… let me see the community page.
Antoine Toulme 00:54:01 Yep, we do.
Michele Mancioppi 00:54:02 Yep.
Antoine Toulme 00:54:03 I would rather… Oh, the whole thing.
Tedsuo 00:54:06 Yeah, I'd rather link… Because all this stuff, we write it and triplicate it, and then it fucking gets out of date.
Antoine Toulme 00:54:16 Yeah.
Tedsuo 00:54:19 Okay.
Antoine Toulme 00:54:20 Is there a reason this is a Google Doc?
Tedsuo 00:54:24 I'm gonna turn it into… it's just easier to collaborate in a.
Antoine Toulme 00:54:29 Other than it'll be done to Markdown and be pushed into the community repo, is that right? Yep, yep, it'll go as a product. Okay, gotcha, okay, okay, I understand now, okay.
Tedsuo 00:54:37 I have all the other project files, and I'm just gonna be like.
We never wrote this thing when we added it, so we're just adding it now.
This is not… this is… I'm gonna tell people, like, this has already been approved, no one made a project file, so we're doing it now.
Antoine Toulme 00:54:51 Well, no one told us. Is there a… another.
Tedsuo 00:54:53 Totally fine. Yeah, no, I mean, I want to do a bit of a post-mortem with GCTC and be like, wow, this… this thing blew through. Maybe it… and it seems like it blew through post us setting that stuff up, so… a little bit like what happened, but…
Antoine Toulme 00:55:07 Is there a list of things?
Oh, my God, I've never been to this.
Tedsuo 00:55:11 Not on, not on the, not on the, donations.
I feel like we haven't been doing a great job managing donations.
I feel like it's… it can be… because people are so busy.
donations, I feel like the people donating are often in a position where they're, like, maybe waiting for GC or TPC people, it doesn't feel as organized as it should be.
But…
Antoine Toulme 00:55:39 Are you talking about the projects folder under the community repository?
Tedsuo 00:55:43 Yeah, that's where I'm gonna put this.
Antoine Toulme 00:55:45 If I was to read this, I would be very, very unhappy with, like, I need to go and fix Collector V1 right now.
It's filled with TBD links, and… Whoa.
Like, it's dangerous.
Tedsuo 00:55:58 I would like Sigs to… to start… going back and kind of, like, updating this, but again, I'm not… I'm not trying to fix the path, I'm trying to make the new SIGs, like…
Antoine Toulme 00:56:09 Okay, then…
Tedsuo 00:56:10 So we've got this SIG, we've got the browser SIG. I'm saying if we're spinning up new things, let's… Let's have our project files up to date. Let's, like… Try to make the meetings… snappy, let's try to have deadlines, let's try to have, like, not endless projects, but short-scale projects, right? That's why we don't want to just have SIGs, because a SIG is this, like, endless thing. It's just a group of people that meets. We want to have A project with a deadline.
like, some goal that the SIG is trying to meet, and an…
Antoine Toulme 00:56:42 But, sir, this is open source. But, okay, fine, sure, okay.
Tedsuo 00:56:46 I mean, it's… but it's, like, it's open source at massive scale, right? It's open source at a scale where, like, not doing these organizing things are causing some problems.
Antoine Toulme 00:56:57 The kiosk is a function of open source. It's actually valid.
Tedsuo 00:57:02 It is, it is, it is. But, like, what… it's more about, like.
When we have these groups of people, for example, if you have, like, a… if you've broken the project down into smaller pieces.
And you have goals and targeting, that actually does wonders for reducing the amount of, like, bike shedding and astronauting.
Because the people who want to ship now have, like, a thing they can point to. They have a sign they can point to on the wall. They're like, we're trying to ship just this.
Antoine Toulme 00:57:31 I'm just…
Tedsuo 00:57:33 the browser sig was going round and round, because there's so many things we could build in the browser, right? Like, we could build a protocol, like a mobile protocol. People want something like that. There's, like, all this stuff.
Michele Mancioppi 00:57:43 Wait, wait, is that…
Tedsuo 00:57:46 scope. We have to cut scope. What are we gonna do? And we cut it down to, like.
Michele Mancioppi 00:57:50 Hey, just a second, Ted. That was actually something people discussed?
Tedsuo 00:57:55 Yeah, I have to think people disgust.
Antoine Toulme 00:57:57 He's gonna go to that signal. Okay.
Bastian Krol 00:58:01 No one, no, we're not doing it in the SIG. That's the thing, if you look at the browser SIGs.
Antoine Toulme 00:58:05 Project logical.
Tedsuo 00:58:07 It says, what are we doing? Right now, we're gonna build instrumentation first, because that's the thing that's missing. Everything in the stack exists, but is not optimal.
But it does work.
So we're gonna start with a piece that's missing, which is the instrumentation and the semantic conventions, and we're just gonna focus on that. We're not gonna work on a protocol right now, because that would…
Antoine Toulme 00:58:28 at the.
Tedsuo 00:58:28 That would suck different people in, like, Michelle, and, like, you know, all kinds of people who don't give a shit about the browser are gonna care about that.
Michele Mancioppi 00:58:36 Oh, no, I would stay away, like, the plague, but that's a different topic.
You then want another protocol? I am probably gonna have…
Tedsuo 00:58:47 You see the advantage of, like, having SIGs? Like, the more we think about it and break down, the better roadmap we… our roadmap is better in the browser SIG. We're working on the most important thing because we did the work of trying to break it into pieces.
Antoine Toulme 00:59:02 Yeah, Ted, the only thing I would want you to question this with is that you are competing with the open internet, and anyone can create a GitHub project and say, fuck you, all this bureaucracy fucking sucks, I'm just gonna get on top of this, and do my own thing, and you.
Michele Mancioppi 00:59:16 Yeah, but in this case, it's actually not realistic.
Because… We will need support from other SIGs to get non-Java, non-Node.js languages off the ground.
Tedsuo 00:59:30 Yeah, exactly.
I think it's great if Sigs can just ship on their own, right? And that was part of the… part of the bureaucracy was, like.
Yeah, I don't know, it'd be great to have less bureaucracy, but… I'm also excited about how OpenTelemetry… we did a lot of work around not forcing you into our implementations.
Right? If someone wants to build a better… if they're like, this Python SDK sucks. This… whatever… this OTEL component sucks. I just… I think I could just make a better SDK if I just ignored your fucking spec and everything else.
And someone can just go build that, and compete with us, and I actually think that's a good thing.
And I'm intrigued to see when and how it starts happening.
Anyways…
Michele Mancioppi 01:00:19 with the rotor collector, the one in Ruby, right?
Tedsuo 01:00:27 Right, yeah, for whatever reason, everyone wants to keep rebuilding the collector, which is, like, the least interesting thing to rebuild, but whatever.
Antoine Toulme 01:00:35 That's true. Marginal gains a bit.
That's true.
Tedsuo 01:00:39 Yeah, I could go on for, I mean…
Michele Mancioppi 01:00:44 Being the linchpin of the entire project, of course, the most glorious one.
Antoine Toulme 01:00:50 Yeah.
Okay.
Tedsuo 01:00:52 Yeah, but it's more like, I would love to see, like, non-native SDKs, right?
Right?
And… All it is is a fucking ring.
Hard.
You know, and, like, no features. You don't get any features. All you get is Protobuff.
like, pushed out the door as fast as possible in C++, that's literally all this thing does, and then hooked it up to the Open Tracing API.
And it was, like, blazing fast.
Are there a bunch of people who are like, fuck you, I'd never touch your C++ monstrosity? Yes. But are there people… People who are like, I don't care about features or options or anything, all I care about is how fast can I ship the telemetry off the box. And there's no one implementation that's gonna make both people happy, right? The people who want, like, a language-native framework, and the people who just want Willing to, like, put up with painful things to get the speed.
Anyways…
Michele Mancioppi 01:01:56 Cool.
Antoine Toulme 01:01:58 I'm catching up.
Tedsuo 01:01:58 I think we're good. I can clean up… I can clean up the rest of this… bullshit.
In this, and I will submit it.
Michele Mancioppi 01:02:05 If you… if you want to sound off your pitch, when… you know where to find us.
Tedsuo 01:02:10 Yeah, I'm actually… I'm gonna be in Brussels next week. I don't know if that's close to any of you.
Michele Mancioppi 01:02:18 I don't know.
Antoine Toulme 01:02:21 Nope. I'm in San Jose, California.
Tedsuo 01:02:23 Anyone in London? Where any of you could… You're in Southern California?
Where… where are you, Michelle?
Michele Mancioppi 01:02:30 Alrighty.
Tedsuo 01:02:32 Near Germany?
Michele Mancioppi 01:02:32 I mean, the southwest? No, I'm Italian, but even the southwest of Germany.
Tedsuo 01:02:37 Okay.
Michele Mancioppi 01:02:39 Like, I am not even gonna tell you the name of the city, because not even Bastian, who's German, probably knows it.
Bastian Krol 01:02:47 Yeah, so you're in the card school.
Aw.
Michele Mancioppi 01:02:50 Yeah, way too ruin my rhetoric argument, man. Thank you.
Tedsuo 01:02:55 Is that the same place? I went to the Instana office years ago. Is it the same town?
Michele Mancioppi 01:02:59 again. It's actually in, like… the other side of Germany in, North Weiss.
Tedsuo 01:03:06 Okay.
What about you, Bashin? Where are you located?
Bastian Krol 01:03:10 I'm in Dortmund, also Germany, so that's somewhat close to Zoling, which is also a very unremarkable drift town.
Tedsuo 01:03:19 Cool.
Okay, well, no one's in Brussels. Or London.
That's fine.
Bastian Krol 01:03:26 No.
Bye.
10 time zone, at least.
Antoine Toulme 01:03:33 Alright. It was great catching up.
Michele Mancioppi 01:03:34 To drop off. Yeah. Bye!
Bastian Krol 01:03:38 Bye-bye!
